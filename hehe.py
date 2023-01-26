import matplotlib.pyplot as plt
from firedrake import *
from firedrake_adjoint import *

mesh = Mesh("motion_mesh1.msh")

# NBVAL_IGNORE_OUTPUT
fig, axes = plt.subplots()
triplot(mesh, axes=axes)
axes.axis("off")
axes.set_aspect("equal")
axes.legend(loc="upper right");

V = VectorFunctionSpace(mesh, "Lagrange", 2)
Q = FunctionSpace(mesh, "Lagrange", 1)
W = V*Q

v, q = TestFunctions(W)
u, p = TrialFunctions(W)

nu = Constant(1)     # Viscosity coefficient

x, y = SpatialCoordinate(mesh)
u_inflow = as_vector([y*(10-y)/25.0, 0])

noslip = DirichletBC(W.sub(0), (0, 0), (7, 8))
inflow = DirichletBC(W.sub(0), interpolate(u_inflow, V), 7)
static_bcs = [inflow, noslip]

g = Function(V, name="Control")
controlled_bcs = [DirichletBC(W.sub(0), g, 8)]
bcs = static_bcs + controlled_bcs

a = nu*inner(grad(u), grad(v))*dx - inner(p, div(v))*dx - inner(q, div(u))*dx
L = Constant(0)*q*dx

w = Function(W)
solve(a == L, w, bcs=bcs, solver_parameters={"mat_type": "aij",
                                             "ksp_type": "preonly",
                                             "pc_type": "lu",
                                             "pc_factor_shift_type": "inblocks"})


# NBVAL_IGNORE_OUTPUT
u_init, p_init = w.split()

fig, axes = plt.subplots(nrows=2, sharex=True, sharey=True)
streamlines = streamplot(u_init, resolution=1/3, seed=0, axes=axes[0])
fig.colorbar(streamlines, ax=axes[0], fraction=0.046)
axes[0].set_aspect("equal")
axes[0].set_title("Velocity")

contours = tricontourf(p_init, 30, axes=axes[1])
fig.colorbar(contours, ax=axes[1], fraction=0.046)
axes[1].set_aspect("equal")
axes[1].set_title("Pressure");

u, p = split(w)
alpha = Constant(10)

J = assemble(1./2*inner(grad(u), grad(u))*dx + alpha/2*inner(g, g)*ds(8))
m = Control(g)
Jhat = ReducedFunctional(J, m)

get_working_tape().progress_bar = ProgressBar

g_opt = minimize(Jhat)