import numpy as np
from matplotlib import pyplot as plt

N2PER = 98.4
CH4PER = 1.4
H2PER = .2

SurfStdTemp = 93.7
LapseRate040 = -.0005
ChangeRate4060 = .0004
ChangeRate6080 = .0025
SurfStdPress = 146700
SpecificHeatRat = 1.45
g = 1.352

N2MOLMASS = 28.02
CH4MOLMASS = 16.042
H2MOLMASS = 2.016

AMolMass = N2PER / 100 * N2MOLMASS + CH4PER / 100 * CH4MOLMASS + H2PER / 100 * H2MOLMASS
SpecGasConst = 8.314 / AMolMass * 1000

def Temperature(alt):
    std = SurfStdTemp
    if alt >= 60*1000 and alt < 80*1000:
        temp = SurfStdTemp + LapseRate040 * 40 * 1000 + ChangeRate4060 * 20 * 1000 + ChangeRate6080 * (alt - 60*1000)
    elif alt >= 40*1000 and alt < 60*1000:
        temp = SurfStdTemp + LapseRate040 * 40 * 1000 + ChangeRate4060 * (alt - 40*1000)
    elif alt < 40*1000 and alt >= 0:
        temp = SurfStdTemp + LapseRate040 * alt
    else:
       temp = "Altitude must be within 0 and 80000 meters"
    return temp

def Pressure(alt):
    std = SurfStdPress
    press40 = np.e ** (-g / (SpecGasConst*LapseRate040) * np.log(Temperature(40*1000) / Temperature(0))) * SurfStdPress
    press60 = np.e ** (-g / (SpecGasConst*ChangeRate4060) * np.log(Temperature(60*1000) / Temperature(40*1000))) * press40
    if alt >= 0 and alt < 40 * 1000:
        press = np.e ** (-g / (SpecGasConst*LapseRate040) * np.log(Temperature(alt) / Temperature(0))) * SurfStdPress
    elif alt >= 40 * 1000 and alt < 60 * 1000:
        press = np.e ** (-g / (SpecGasConst*ChangeRate4060) * np.log(Temperature(alt) / Temperature(40*1000))) * press40
    elif alt >= 60*1000 and alt < 80*1000:
        press = np.e ** (-g / (SpecGasConst*ChangeRate6080) * np.log(Temperature(alt) / Temperature(60*1000))) * press60
    else:
       press = "Altitude must be within 0 and 80000 meters"
    return press

def Density(alt):
    return Pressure(alt) / (Temperature(alt) * SpecGasConst)

plot1 = plt.figure(1)
y1 = np.arange(0, 80*1000)
temps = []
for i in range(80*1000):
    temps.append(Temperature(i))
x1 = temps
plt.title("Temperature vs Altitude")
plt.xlabel("Temperature (K)")
plt.ylabel("Altitude (m)")
plt.plot(x1,y1)

plot2 = plt.figure(2)
y2 = np.arange(0, 80*1000)
presses = []
for i in range(80*1000):
    presses.append(Pressure(i))
x2 = presses
plt.title("Pressure vs Altitude")
plt.xlabel("Pressure (Pa)")
plt.ylabel("Altitude (m)")
plt.plot(x2,y2)

plot3 = plt.figure(3)
y3 = np.arange(0, 80*1000)
dens = []
for i in range(80*1000):
    dens.append(Density(i))
x3= dens
plt.title("Density vs Altitude")
plt.xlabel("Density (kg/m^3)")
plt.ylabel("Altitude (m)")
plt.plot(x3,y3)

print("Pressure at 50km: " + str(Pressure(50*1000)) + " Pa")
print("Pressure at 70km: " + str(Pressure(70*1000)) + " Pa")
print("Density at 50km: " + str(Density(50*1000)) + " kg/m^3")
print("Density at 70km: " + str(Density(70*1000)) + " kg/m^3")
plt.show()