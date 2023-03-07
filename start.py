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
x = [random.uniform(1, 100) for n in range(20)]
y = [random.uniform(1, 100) for n in range(20)]

#dt = 282*pow(10, 6)  / 16400      # t=x/v where v is velocity [m/s] and x is the leght of saturns rings [m]

#v_x = x * dt
#v_y = 0

# then do move them one point so that


# Make the data points move with correct velocity and gravitational field

class Particles():
    def __init__(self, p, v, m):
        self.p = p      # Position
        self.v = v      # Velocity
        self.m = m      # Mass

dx = np.ones_like(x)
dy = np.zeros_like(y)

# Plot the points and arrows
fig, ax = plt.subplots()

plt.scatter(x, y, color = 'red')
plt.quiver(x, y, dx, dy, scale =20)

for i in range(2):
    x_new = [random.uniform(1, 100) for n in range(200)] 
    y_new = [random.uniform(1, 100) for n in range(200)] 
    dx_new = np.ones_like(x)
    dy_new = np.zeros_like(y)

    sc = plt.scatter(x, y, color = 'red')
    plt.quiver(x_new, y_new, dx_new, dy_new, scale=20)
    plt.pause(2)

    for j in range(2):
        x[j] += [random.uniform(1, 100) for n in range(200)] * 2
        j[j] += [random.uniform(1, 100) for n in range(200)] * 2
    #ax.scatter(x, y, color = 'red')
    sc.set_offsets(np.c_[x, y]) 
    plt.pause(2)
    ax.clear()

plt.show()
