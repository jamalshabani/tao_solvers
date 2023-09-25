from firedrake import *
mesh = Mesh("hexagonal.msh")
Id = Identity(mesh.geometric_dimension()) #Identity tensor

V = FunctionSpace(mesh, 'CG', 1)
f = Constant(1.0)
#f = Function(V)
f = interpolate(f, V)

print(assemble(f*dx(3)))