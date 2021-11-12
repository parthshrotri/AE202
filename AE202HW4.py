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

###################PROBLEM 2###################


###################PROBLEM 3###################

###################PROBLEM 4###################

###################PROBLEM 5###################
