import numpy as np

#Initial position
y0 = 2

#Initial angle
a0 = 3

#Length from y0 to y1
L = 3

#Radius of lens
R0 = 30
R1 = float('inf')

#Refractive index of air
n0 = 1

#Refractive index of lens
n1 = 1.5

#Initial position and angle
A0 = np.array([[y0],[a0]])

#Translation Matrix
MTrans = np.array([[1, L],[0,1]])
ATrans = MTrans.dot(A0)

#Refraction into the lens
MRefract0 = np.array([[1, 0],[(n0-n1)/(n1*R0), n0/n1]])
ARefract0 = MRefract0.dot(A0)

#Refraction out the lens
MRefract1 = np.array([[1, 0],[(n1-n0)/(n0*R1), n1/n0]])
ARefract1 = MRefract1.dot(A0)

#Reflection at spherical surface
MReflect = np.array([[1, 0],[2/R0, 1]])
AReflect = MReflect.dot(A0)

#Thick lens Matrix
MThick = MRefract1.dot(MTrans).dot(MRefract0)

#Results
print('Translation matrix :', MTrans)
print('Refractive matrix into the surface :', MRefract0 )
print('Refraction matrix out from the surface :', MRefract1)
print('Reflection matrix :', MReflect)
print('Thick lens matrix :', MThick)
