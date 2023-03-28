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
m_p = 1e-16 #rho / V                   # Mass of paricles 

# Generating random particle in a plot
np.random.seed(0)  # for reproducibility
x = [random.uniform(-100, 100) for n in range(50)]
y = [random.uniform(-100, 100) for n in range(50)]

# Kepler's third law
T = math.sqrt(4 * pow(math.pi, 2) / (G * M) * pow(r, 3))

# Defining omega
Omega = 2 * math.pi / T

# Gravitational force
F_g = G * M * m_p / pow(r, 2)

# Gravitational acceleration of the particle
g_g = F_g / m_p

# Velocity for x and y direction
v_x = []
v_y = []

for j in range(len(y)):
   vx =  - 2 / 3 * Omega *  y[j]
   v_x.append(vx)
   
   vy = -g_g *0.1
   v_y.append(vy)

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
plt.ylabel('Discatnce from Satrurn (km??)')
plt.xlabel('m')

# Plotting the arrows
dx = arrows(dx, x, y)
plt.quiver(x, y, dx, dy, scale = 10)

# Making the points move
for i in range(1000):
    x = [x[i] + v_x[i] for i in range(len(x))]
    y = [y[i] + v_y[i] for i in range(len(y))]
    points.set_data(x, y)
    plt.pause(0.001)

plt.show()
