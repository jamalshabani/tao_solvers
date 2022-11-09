from firedrake import *
from firedrake_adjoint import *
from petsc4py import PETSc
import numpy as np


N = 32
mesh = UnitSquareMesh(N, N)
V = FunctionSpace(mesh, "CG", 1)

f = Function(V)
f.assign(Constant(1.0))

R = FunctionSpace(mesh, "R", 0)
c = Function(R)
c.project(Constant(1.0))

u = Function(V)
p = Function(V)
v = TestFunction(V)
bc = DirichletBC(V, 0.0, "on_boundary")

xc, yc = SpatialCoordinate(mesh)
u_s = 1.0 / (2.0 * pi**2) * sin(pi * xc) * sin(pi * yc)

alpha = Constant(1.0)
lmbda = Constant(1.0e-6)

R_fwd = inner(grad(u), grad(v))*dx - c * f * v *dx


def formObjGradient(tao, x, G):
    with c.dat.vec as c_vec:
        x.copy(c_vec)

    solve(R_fwd == 0, u, bc)

    J = assemble(0.5 * alpha * inner(u - u_s, u - u_s) * dx + 0.5 * lmbda * c**2 * dx)
    Jhat = ReducedFunctional(J, Control(c))

    dJdf = Jhat.derivative()
    G.zeroEntries()
    with dJdf.dat.vec_ro as dJdf_vec:
        dJdf_vec.copy(G)

    return J


tao = PETSc.TAO().create(PETSc.COMM_SELF)
tao.setType('cg')
tao.setObjectiveGradient(formObjGradient)
tao.setFromOptions()

with c.dat.vec as x_vec:
    tao.solve(x_vec)
