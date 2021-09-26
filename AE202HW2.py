import numpy as np
from matplotlib import pyplot as plt

########### PROBELM 1 ###########
print()
print("PROBLEM 1")
V = 250
A = 12000
scale = 1/6
Tmodel = 253
Tairliner = 216.66

rho = .3108
viscosityAirliner = 1.7984*10**(-5)
viscosityModel = viscosityAirliner / ((Tairliner / Tmodel) ** (1/2))

vmodel = V / ((Tairliner / Tmodel) ** (1/2))

densityModel = ((rho * V * 6 / viscosityAirliner) * viscosityModel) / (vmodel)

P = densityModel * 287 * Tmodel
print("Velocity in wind tunnel: " + str(vmodel) + "m/s")
print("Pressure in wind tunnel: " + str(P) + "Pa")

########### PROBELM 2 ###########
print()
print("PROBLEM 2")
C = .4
P = 93 * 1000
T = 290
R = 287
v = 31 

cl3 = 0.3201
cl11 = 1.1668
clneg2 = -0.2144

cd3 = .00640
cd11 = 0.01690
cdneg2 = 0.00581

cm3 = 0.0048
cm11 = 0.0091
cmneg2 = -0.0030

rho = P/(R*T)
print("Assume standard viscosity")
Re = rho * v * C / (1.7894*10**(-5))

L3 = cl3 * (1/2) * rho * v**2 * C
L11 = cl11 * (1/2) * rho * v**2 * C
Lneg2 = clneg2 * (1/2) * rho * v**2 * C

D3 = cd3 * (1/2) * rho * v**2 * C
D11 = cd11 * (1/2) * rho * v**2 * C
Dneg2 = cdneg2 * (1/2) * rho * v**2 * C

M3quart = cm3 * (1/2) * rho * v**2 * C**2
M11quart = cm11 * (1/2) * rho * v**2 * C**2
Mneg2quart = cmneg2 * (1/2) * rho * v**2 * C**2

print("Lift at 3º: " + str(L3) + "N/m")
print("Drag at 3º: " + str(D3) + "N/m")
print("Moment about the quarter chord at 3º: " + str(M3quart) + "N")
print()
print("Lift at 11º: " + str(L11) + "N/m")
print("Drag at 11º: " + str(D11) + "N/m")
print("Moment about the quarter chord at 11º: " + str(M11quart) + "N")
print()
print("Lift at -2º: " + str(Lneg2) + "N/m")
print("Drag at -2º: " + str(Dneg2) + "N/m")
print("Moment about the quarter chord at -2º: " + str(Mneg2quart) + "N")

########### PROBLEM 3 ###########
print()
print("PROBLEM 3")

plot1 = plt.figure(1)

Wspan = 10.40
Warea = 16.60
Ar = 6.5
Weight = 1650
OswaldEff = .8
Cd0 = .01
Clmax = 1.3

k = 1 / (np.pi*OswaldEff*Ar)
print("Induced Drag Coefficient: " + str(k))

cl = np.arange(-Clmax, Clmax, .01)
cd = Cd0 + k*(cl**2)

plt.title("Cl vs. Cd for Standard PC-7")
plt.xlabel("Cl")
plt.ylabel("Cd")
plt.plot(cl,cd)

plot2 = plt.figure(2)
newAR = 5

knew = 1 / (np.pi*OswaldEff*newAR)
cdnew = Cd0 + k*(cl**2)

plt.title("Cl vs. Cd for Aerobatic PC-7")
plt.xlabel("Cl")
plt.ylabel("Cd")
plt.plot(cl,cdnew)
plt.show()