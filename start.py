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
x = [random.uniform(1, 100) for n in range(200)]
y = [random.uniform(1, 100) for n in range(200)]

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
plt.scatter(x, y, color ='red')
plt.quiver(x, y, dx, dy, scale=20)

sc = plt.scatter(x, y)

for i in range(50):
    x += [random.uniform(1, 100) for n in range(200)] * 2
    y += [random.uniform(1, 100) for n in range(200)] * 2
    sc.set_offsets(np.c_[x, y]) 
    plt.pause(2)

plt.show()
