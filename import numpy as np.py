import numpy as np

C = .4
P = 93 * 1000
T = 290
R = 287
v = 31 

cl3 = .3
cl11 = 1.2
clneg2 = -.2

cd3 = .008
cd11 = .025
cdneg2 = .007

cm3 = .006
cm11 = .011
mneg2 = .005

rho = P/(R*T)
Re = rho * v * C / (1.7894*10**(-5))

L3 = cl3 * (1/2) * rho * v**2 * C
L11 = cl11 * (1/2) * rho * v**2 * C
Lneg2 = clneg2 * (1/2) * rho * v**2 * C

D3 = cd3 * (1/2) * rho * v**2 * C
D11 = cd11 * (1/2) * rho * v**2 * C
Dneg2 = cdneg2 * (1/2) * rho * v**2 * C

print(L3)
print(L11)
print(Lneg2)

print(D3)
print(D11)
print(Dneg2)

#M3quart = cm3 * (1/2) * rho * v**2 * C
#M11quart = cm3 * (1/2) * rho * v**2 * C
#Mneg2quart = cm3 * (1/2) * rho * v**2 * C