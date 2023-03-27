import math 
import numpy as np
import matplotlib.pyplot as plt 
import random 
from matplotlib import animation 

# Useful values

r = 58232*pow(10, 3)            # radius of Saturn with units [m]
M = 5.683*pow(10, 26)           # mass of Saturn with units [kg]
g = 10.44                       # gravity ofSaturn with units [m/s^2]
G = 6.674*pow(10, -11)          # gravitational constant with units [m^3 kg^-1 s^-2]
rho = 1000                      # density of particle in Saturn's rings with units [kg/m^3]
r_d = 500 * pow(10, -9)         # Average radius of particles with units [m]
V = 4/3 * math.pi * pow(r_d, 3) # Volume of particles 
m_p = rho / V                   # Mass of paricles 

# Generating random particle in a plot
x = [random.uniform(-100, 100) for n in range(50)]
y = [random.uniform(-100, 100) for n in range(50)]

# Kepler's third law
T = math.sqrt( 4 * pow(math.pi, 2) / (G * M) * pow(r, 3))

# Defining omega
Omega = 2 * math.pi / T

# Velocity in the x-direction
v_x = np.array([-2/3 * Omega * y_i for y_i in y])

# Definig a list for kinetic energy
KE = []

for i in range(len(v_x)):
    kineticenergy = 0.5 * np.power(v_x[i], 2)
    KE.append(kineticenergy)

# Definig a list for time
timepos = []
deltaT = 2000

for i in range(len(v_x)):
    timestep = deltaT * i
    timepos.append(timestep)

# Plotting a graph showing kinetic energy over a period of time 
plt.plot(timepos, KE, label='Kinetic energy') 
plt.ylabel('Kinetic Energy (J)')
plt.xlabel('Time (s)')
plt.ylim([-1, 1])
plt.legend()
plt.show()
