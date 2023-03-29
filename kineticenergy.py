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
m_p = 513                       # Mass of paricles [kg]

# Generating random particle in a plot
x = [random.uniform(-100, 100) for n in range(50)]
y = [random.uniform(-100, 100) for n in range(50)]

# Kepler's third law
T = math.sqrt( 4 * pow(math.pi, 2) / (G * M) * pow(r, 3))

# Defining omega
Omega = 2 * math.pi / T

# Velocity in the x-direction
v_x = np.array([-2/3 * Omega * (6630 * pow(10, 3) + y_i) for y_i in y])

# Defining initial kinetic energy
KE_0 = 0.5 * m_p * np.sum(np.power(v_x, 2))

# Defining lists for kinetic energy and time
KE = [KE_0]
time = [0]

# Loop for calculating kinetic energy and time over 1 hour
dt = 10
for t in range(1, 3600, dt):
    # Updating the particles positions and velocities
    x += v_x * dt
    y += np.zeros_like(y)
    v_x += np.zeros_like(v_x)
    time.append(t)
    
    # Calculating kinetic energy
    KE_t = 0.5 * m_p * np.sum(np.power(v_x, 2))
    KE.append(KE_t)
    

# Plotting a graph showing conservation of kinetic energy over time
plt.figure(figsize=(6, 4))
plt.plot(time, KE, color='purple') 
plt.ylabel('Kinetic Energy (J)')
plt.xlabel('Time (s)')

plt.show()
