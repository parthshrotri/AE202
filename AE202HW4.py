import numpy as np
from matplotlib import pyplot as plt
from  sympy import *

###################CONSTANTS###################

muEarth = 3.986*(1000**3)*10**5              #m^3/s^2
muSun = 1.327*(1000**3)*10**11               #m^3/s^2
radiusEarth = 6371 * 1000               #meters
perihelionEarth = 147.09 *1000 * 10**6  #meters
aphelionEarth = 152.10 * 1000 * 10**6   #meters

minAlt = 200*1000                        #meters
maxAlt = 40000*1000                     #meters

###################PROBLEM 1###################
print("Problem 1")
def acceleration(dist, gravParam):
    return gravParam / (dist**2) #acceleration in m/s^2

def velocity(dist, gravParam):
    return (gravParam/(1000**3) / (dist/1000))**(1/2) #velocity in km/s

def period(dist, gravParam):
    return  (2*np.pi * dist**(3/2) / (gravParam**(1/2)))/(60*60)#period in hours

AltitudeRange = radiusEarth + minAlt + np.arange(maxAlt-minAlt)

accelerationVals = acceleration(AltitudeRange, muEarth)
velocityVals = velocity(AltitudeRange, muEarth)
periodVals = period(AltitudeRange, muEarth)

plot1 = plt.figure(1)
plt.title("Orbital Altitude vs Acceleration")
plt.xlabel("Altitude (km)")
plt.ylabel("Acceleration (m/s^2)")
plt.plot((AltitudeRange-radiusEarth)/1000 ,accelerationVals)

plot2 = plt.figure(2)
plt.title("Orbital Altitude vs Velocity")
plt.xlabel("Altitude (km)")
plt.ylabel("Velocity (km/s)")
plt.plot((AltitudeRange-radiusEarth)/1000 ,velocityVals)

plot3 = plt.figure(3)
plt.title("Orbital Altitude vs Period")
plt.xlabel("Altitude (km)")
plt.ylabel("Period (hrs)")
plt.plot((AltitudeRange-radiusEarth)/1000 ,periodVals)
plt.show()
print()
###################PROBLEM 2###################
print("Probelm 2")
rA = 13910
rP = 7900

hp = 400
p = 13542

r = 7000
v = 13200

rVec = [-4684.5, 5088.2, 872.2]
vVec = [4.0978, 4.5358, 4.4513]

def typeOfOrbitA(apoapsis, periapsis):
    if apoapsis == periapsis:
        return "circular"
    else:
        return "elliptic"

def typeOfOrbitB(periapsis, P):
    e = symbols('e')
    eq = Eq((periapsis+radiusEarth/1000)*(1+e), P)
    sol = solve(eq)
    e = np.absolute(sol[0])
    return determineOrbitType(e)
    

def typeOfOrbitC(position, velocity):
    a, e = symbols('a e')
    eq1 = Eq((-muEarth/(1000**3))/(2*a), (1/2)*velocity**2 - (muEarth/(1000**3)/position))
    sol1 = solve(eq1)
    a = sol1[0]
    h = position*velocity
    eq2 = Eq(h**2/(muEarth/(1000**3)), a*(1-e**2))
    sol2 = solve(eq2)
    e = np.absolute(sol2[0])
    return determineOrbitType(e)

def typeOfOrbitD(position, velocity):
    rMag = (position[0]**2 + position[1]**2 + position[2]**2)**(1/2)
    vMag = (velocity[0]**2 + velocity[1]**2 + velocity[2]**2)**(1/2)
    a, e = symbols('a e')
    eq1 = Eq((-muEarth/(1000**3))/(2*a), (1/2)*vMag**2 - (muEarth/(1000**3)/rMag))
    sol1 = solve(eq1)
    a = sol1[0]
    h = rMag*vMag
    eq2 = Eq(h**2/(muEarth/(1000**3)), a*(1-e**2))
    sol2 = solve(eq2)
    e = np.absolute(sol2[0])
    return determineOrbitType(e)

def determineOrbitType(e):
    if e<=.001 :
        return "circular"
    elif .001<e and e<1:
        return "elliptic"
    elif e == 1:
        return "parabolic"
    else:
        return "hyperbolic"

print("a. " + typeOfOrbitA(rA, rP))
print("b. " + typeOfOrbitB(hp, p))
print("c. " + typeOfOrbitC(r, v))
print("d. " + typeOfOrbitD(rVec, vVec))
print()
###################PROBLEM 3###################
print("Probelm 3")
alt = 400
rP = alt + radiusEarth / 1000
vP = ((muEarth/(1000**3))/rP)
print("a. Periapsis altitude is " + str(alt) + "km and velocity is " + str(vP) + "km/s")
vesc = ((2*muEarth/(1000**3))/rP)**(1/2)
vinf = 1.5
vel = (vinf**2 + vesc**2)**(1/2)
print("b. Velocity of " + str(vel) + "km/s")
h = rP * vel
e = symbols('e')
eq = Eq(rP, h**2/(muEarth/(1000**3))/(1+e*cos(0)))
sol = solve(eq)
e = sol[0]
print("c. specific angular momentum: " + str(h) + "km^2/s and eccentricity of " + str(e))
print()

###################PROBLEM 4###################
print("Probelm 4")
apoapsis = 6300
periapsis = 5000
muMars = 42828.372

a = (apoapsis + periapsis)/2
e = (apoapsis - periapsis) / (apoapsis + periapsis)

period = 2*np.pi/np.sqrt(muMars) * a**(3/2)
n = 2*np.pi / period
M = n * (3*60+12)
E, nu = symbols('E nu')
eq1 = Eq(M, E-e*sin(E))
E = .10569823335944637 #solved using graphing calculator as sympy solver could not solve
eq2 = Eq(tan(E/2), tan(nu/2)*sqrt((1-e)/(1+e)))
sol2 = solve(eq2)
nu = sol2[0]
print("True anomaly is " + str(nu) + " radians")
###################PROBLEM 5###################