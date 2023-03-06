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

v_x
v_y

# Make the data points move with correct velocity and gravity field

class Particles():
    def __init__(self, p, v, m):
        self.p = p      # Position
        self.v = v      # Velocity
        self.m = m      # Mass

fig, ax = plt.subplot()

def animate(i):
    #pt = randint(1,9) # grab a random integer to be the next y-value in the animation
    x.append(i)
    y.append(i)

fig = plt.scatter(x, y)

#plt.scatter(x, y, color = 'red')
plt.show()
