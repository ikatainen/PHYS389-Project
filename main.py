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

# Velocity for x direction
v_x = []

for j in range(len(y)):
   v =  - 2 / 3 * Omega * y[j]
   v_x.append(v)

# Defining dx and dy for the arrows 
dx = np.zeros_like(x)
dy = np.zeros_like(y)

def arrows(dx, x, y):
    for i in range(len(y)):
        if y[i] < 0:
            dx[i] = 1
        elif y[i] > 0:
            dx[i] = -1
    return dx

# Plot the points and arrows
fig, ax = plt.subplots()

points, = ax.plot(x, y, 'ro')

# Moonlet 
plt.scatter(0, 0, color = 'black', s = 100)

# Plotting the initail point 
plt.scatter(x, y, color = 'red')

# Plotting the arrows
dx = arrows(dx, x, y)
plt.quiver(x, y, dx, dy, scale = 10)

# Making the points move
for i in range(1000):
    x = [x[i] + v_x[i] for i in range(len(x))]
    points.set_data(x, y)
    plt.pause(0.001)

plt.show()