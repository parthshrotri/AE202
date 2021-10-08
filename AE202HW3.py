import numpy as np
from matplotlib import pyplot as plt
from  sympy import *

#################PROBLEM 1#################
S = 53
AR = 5
e = .83
W = 98100
Cd_0 = .047
TslPerEngine = 34335
rhoSL = 1.225
numEngines = 2
rho10km = .4127

def PowerRequired(rho, v):
    Cl = 2* W / (rho * S * v**2) 
    Cd = Cd_0 + Cl**2 / (np.pi * e * AR)
    PReq = W / (Cl/Cd) * v / 1000
    return PReq
def PowerAvailable(rho, v):
    TAvail = TslPerEngine * rho / 1.225
    PAvail = TAvail * v * numEngines / 1000
    return PAvail
print()
print("Probelm 1")
vel = np.arange(50,350)
PRsl = PowerRequired(rhoSL, vel)
PAsl = PowerAvailable(rhoSL, vel)
plot1 = plt.figure(1)
plt.title("Velocity vs Power at Sea-Level")
plt.xlabel("Velocity (m/s)")
plt.ylabel("Power (kW)")
plt.plot(vel,PRsl, label = "Power Required")
plt.plot(vel,PAsl, label = "Power Available")
plt.legend()


PR10km = PowerRequired(rho10km, vel)
PA10km = PowerAvailable(rho10km, vel)
plot2 = plt.figure(2)
plt.title("Velocity vs Power at 10km")
plt.xlabel("Velocity (m/s)")
plt.ylabel("Power (kW)")
plt.plot(vel,PR10km, label = "Power Required")
plt.plot(vel,PA10km, label = "Power Available")
plt.legend()
plt.show()
print("Max velocity at sea-level: 211 m/s")
print("Max velocity at 10km: 204 m/s")

#################PART G##################
# Given density
# Determine PowerRequired with given density and a range of velocities from 50m/s to 350m/s
# Determine PowerAvailable with given density and a range of velocities from 50m/s to 350m/s
# Create np array storing differences between PowerAvailable and PowerRequired
# Find maximum value in difference array
# Maximum rate of climb is max difference / W
# return maximum rate of climb

def maxRateOfClimb(rho):
    vel = np.arange(50,350)
    PR = PowerRequired(rho, vel) * 1000
    PA = PowerAvailable(rho, vel) * 1000
    diff = PA - PR
    maxDiff = max(diff)
    maxRate = maxDiff / W
    return maxRate

#################PROBLEM 2#################
init_printing()
Cd_0, CL, Cd, Cl, k, CD, AR, e, pi  = symbols('C_d0 C_L C_d C_l k C_D AR e pi')

k = 1/ (pi * e * AR)
Cd = Cd_0 + k*Cl**2
MaxRangeRatio = Cl**(1/2) / Cd
differentiation = diff(MaxRangeRatio, Cl)
crit = solve(Eq(differentiation, 0))
Cl = (AR*Cd_0*e*pi / 3)**(1/2)
Cd = Cd = Cd_0 + k*Cl**2
MaxRangeRatio = Cl**(1/2) / Cd
print()
print("Problem 2")
MaxRangeRatio = factor(simplify(MaxRangeRatio))
print("Before hand simplifying: " + str(MaxRangeRatio))
# Transcribed and hand simplified due to sympy not simplifying exponent of 1.00
MaxRangeRatio = (1/3*Cd_0*pi*e*AR)**(1/4) / (4/3*Cd_0)
print("Simplified: " + str(MaxRangeRatio))

#################PROBLEM 3#################
rho9300 = 0.9247
RunwayLengthFt = 1729
RunwayLengthM = RunwayLengthFt / 3.281
Wlbs = 6000
WNewton = Wlbs * 4.448
ClMax = .9
CD = .071
Sft2 = 324.5
Sm2 = Sft2 / 10.764
uR = .4
T = 14500
Wf = 7500
n = .8
Cp = 7*10**(-6)
g = 9.81

print()
print("Probelm 3")
VStall = (2*WNewton / (rho9300 * S * ClMax))**(1/2)
print("Stall speed: " + str(VStall) + " m/s")
VLo = 1.2*VStall
Vavg = .7 * VLo

Lavg = 1/2 * rho9300 * Vavg**2 * Sm2 * ClMax
Davg = 1/2 * rho9300 * Vavg**2 * Sm2 * CD

print("Lift at Vavg: " + str(Lavg) + "N")
print("Drag at Vavg: " + str(Davg) + "N")

TakeOffDistance = VLo**2 * W / (2*g*(T - (Davg + uR*(WNewton - Lavg))))
print("Takeoff distance: " + str(TakeOffDistance) + " m")
print("Can aircraft take off? " + str(TakeOffDistance < RunwayLengthM))

Range = (n / Cp) * (ClMax / CD) * np.log(WNewton / (WNewton - Wf))
print("Range: " + str(Range / 1000) + " km")
Endurance = (n / Cp) * (ClMax**(3/2) / CD) * (2*rho9300*Sm2)**(1/2) * ((WNewton - Wf)**(-1/2) - WNewton**(-1/2))
print("Endurance: " + str(Endurance / 60 / 60) + " hours")
print()