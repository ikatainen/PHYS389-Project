import math 
import numpy as np
import matplotlib.pyplot as plt 
import random 
from matplotlib import animation 
 

# Might be useful values
r = 58232*pow(10, 3)            # radius of Saturn with units [m]
M = 5.683*pow(10, 26)           # mass of Saturn with units [kg]
g = 10.44                       # gravity ofSaturn with units [m/s^2]
G = 6.674*pow(10, -11)          # gravitational constant with units [m^3 kg^-1 s^-2]
rho = 1000                      # density of particle in Saturn's rings with units [kg/m^3]
r_d = 500 * pow(10, -9)         # Average radius of particles with units [m]
V = 4/3 * math.pi * pow(r_d, 3) # Volume of particles 
m_p = rho / V                   # Mass of paricles 

# Generating random particle in a plot
x = [random.uniform(-100, 100) for n in range(100)]
y = [random.uniform(-100, 100) for n in range(100)]

# Kepler's third law
T = math.sqrt( 4 * pow(math.pi, 2) / (G * M) * pow(r, 3))

# Defining omega
Omega = 2 * math.pi / T

# Velocity for x direction
v_x = []

for j in range(len(y)):
   v =  - 2 / 3 * Omega * y[j]
   v_x.append(v)

# Defining dx and dy for the arrows 
dx = np.ones_like(x)
dy = np.zeros_like(y)

# Plot the points and arrows
fig, ax = plt.subplots()

points, = ax.plot(x, y, 'ro')

plt.scatter(x, y, color = 'red')
# Plotting the arrows
plt.quiver(x, y, dx, dy, scale =10)

# Making the points move
for i in range(1000):
    x = [x[i] + v_x[i] for i in range(len(x))]
    points.set_data(x, y)
    plt.pause(0.01)

plt.show()
