# http://www.dolfin-adjoint.org/en/latest/documentation/poisson-topology/poisson-topology.html

from firedrake import *
from firedrake_adjoint import *
import ufl
from pyMMAopt import ReducedInequality, MMASolver
import os
import numpy as np
from pyadjoint.reduced_functional_numpy import set_local


V = Constant(0.4)  # volume bound on the control
p = Constant(5)  # power used in the solid isotropic material with penalisation (SIMP) rule, to encourage the control solution to attain either 0 or 1
eps = Constant(1.0e-3)  # epsilon used in the solid isotropic material
alpha = Constant(1.0e-8)  # regularisation coefficient in functional


def k(a):
    """Solid isotropic material with penalisation (SIMP) conductivity
  rule, equation (11)."""
    return eps + (1 - eps) * a ** p

# Next we define the mesh (a unit square) and the function spaces to be used for the control and forward solution.

n = 250
mesh = UnitSquareMesh(n, n)
A = FunctionSpace(mesh, "CG", 1)  # function space for control
P = FunctionSpace(mesh, "CG", 1)  # function space for solution

# Next we define the forward boundary condition and source term.

# class WestNorth(SubDomain):
#     """The top and left boundary of the unitsquare, used to enforce the Dirichlet boundary condition."""

#     def inside(self, x, on_boundary):
#         return (x[0] == 0.0 or x[1] == 1.0) and on_boundary


# the Dirichlet BC; the Neumann BC will be implemented implicitly by dropping the surface integral after integration by parts
# bc = [DirichletBC(P, 0.0, WestNorth())]

bc1 = DirichletBC(P, 0.0, 1) # left (West)
bc4 = DirichletBC(P, 0.0, 4) # top (North)
bc = [bc1, bc4]
f = interpolate(Constant(1.0e-2), P)  # the volume source term for the PDE

# Next we define a function that given a control solves the forward PDE for the temperature. (The advantage of formulating it in this manner is that it makes it easy to conduct Taylor remainder convergence tests.)

def forward(a):
    """Solve the forward problem for a given material distribution a(x)."""
    T = Function(P, name="Temperature")
    v = TestFunction(P)

    F = inner(grad(v), k(a) * grad(T)) * dx - f * v * dx
    solve(F == 0, T, bc, solver_parameters={"newton_solver": {"absolute_tolerance": 1.0e-7,
                                                              "maximum_iterations": 20}})

    return T

# Now we define the __main__ section. We define the initial guess for the control and use it to solve the forward PDE. In order to ensure feasibility of the initial control guess, we interpolate the volume bound; this ensures that the integral constraint and the bound constraint are satisfied.

if __name__ == "__main__":
    a = interpolate(V, A)  # initial guess.
    T = forward(a)  # solve the forward problem once.

# With the forward problem solved once, dolfin_adjoint has built a tape of the forward model; it will use this tape to drive the optimisation, by repeatedly solving the forward model and the adjoint model for varying control inputs.

# A common task when solving optimisation problems is to implement a callback that gets executed at every functional evaluation. (For example, this might be to record the value of the functional so that it can be plotted as a function of iteration, or to record statistics about the controls suggested by the optimisation algorithm.) The following callback outputs each evaluation to VTK format, for visualisation in paraview. Note that the callback will output each evaluation; this means that it will be called more often than the number of iterations the optimisation algorithm reports, due to line searches. It is also possible to implement callbacks that are executed on every functional derivative calculation.

controls = File("output/control_iterations.pvd")
a_viz = Function(A, name="ControlVisualisation")


def eval_cb(j, a):
    a_viz.assign(a)
    controls.write(a_viz)
    # controls << a_viz

# Now we define the functional, compliance with a weak regularisation term on the gradient of the material

J = assemble(f * T * dx + alpha * inner(grad(a), grad(a)) * dx)
m = Control(a)
Jhat = ReducedFunctional(J, m, eval_cb_post=eval_cb)

# This ReducedFunctional object solves the forward PDE using dolfin-adjoint’s tape each time the functional is to be evaluated, and derives and solves the adjoint equation each time the functional gradient is to be evaluated. The ReducedFunctional object takes in high-level Dolfin objects (i.e. the input to the evaluation Jhat(a) would be a dolfin.Function).

# Now let us configure the control constraints. The bound constraints are easy:

lb = 0.0
ub = 1.0

# We want V - \int rho dx >= 0, so write this as \int V/delta - rho dx >= 0
volume_constraint = UFLInequalityConstraint((V - a)*dx, m)

# The volume constraint involves a little bit more work. Following [3E-NW06], inequality constraints are represented as (possibly vector) functions defined such that . The constraint is implemented by subclassing the InequalityConstraint class. (To implement equality constraints, see the documentation for EqualityConstraint.) In this case, our. In order to implement the constraint, we have to implement three methods: one to compute the constraint value, one to compute its Jacobian, and one to return the number of components in the constraint.

class VolumeConstraint(InequalityConstraint):
    """A class that enforces the volume constraint g(a) = V - a*dx >= 0."""

    def __init__(self, V):
        self.V = float(V)

        # The derivative of the constraint g(x) is constant (it is the diagonal of the lumped mass matrix for the control function space), so let’s assemble it here once. This is also useful in rapidly calculating the integral each time without re-assembling.

        self.smass = assemble(TestFunction(A) * Constant(1) * dx)
        self.tmpvec = Function(A)

    def function(self, m):
        set_local(self.tmpvec, m)     # ufl.log.UFLException: Only full slices (:) allowed.
        # self.tmpvec.vector().set_local(m.vector().array())  # AttributeError: 'CoordinatelessFunction' object has no attribute 'inner'
        # self.tmpvec.vector().set_local(m.vector()) # seeting an array element with a sequence
        

    # Compute the integral of the control over the domain

        integral = self.smass.inner(self.tmpvec.vector())
        # integral = self.smass.inner(self.tmpvec)
        # integral = inner(self.smass, self.tmpvec)
        if MPI.rank(MPI.comm_world) == 0: # not doing this in parallel
            print("Current control integral: ", integral)
        return [self.V - integral]

    def jacobian(self, m):
        return [-self.smass]

    def output_workspace(self):
        return [0.0]

    def length(self):
        """Return the number of components in the constraint vector (here, one)."""
        return 1

# Now that all the ingredients are in place, we can perform the optimisation. The MinimizationProblem class represents the optimisation problem to be solved. We instantiate this and pass it to ipopt to solve:

problem = MinimizationProblem(Jhat, bounds=(lb, ub), constraints=VolumeConstraint(V))

parameters = {"maximum_iterations": 100}
# solver = IPOPTSolver(problem, parameters=parameters)
solver = MMASolver(problem, parameters=parameters)
a_opt = solver.solve()

# File("output/final_solution.pvd") << a_opt
File("output/final_solution.pvd").write(a_opt)
# xdmf_filename = XDMFFile(MPI.comm_world, "output/final_solution.xdmf")
# xdmf_filename.write(a_opt)

