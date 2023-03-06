import math 
import numpy as np
import matplotlib.pyplot as plt 
import random 
 

# Might be useful values
r = 58232*pow(10, 3)            #radius of Saturn with units [m]
M = 5.683*pow(10, 26)           #mass of Saturn with units [kg]
g = 10.44                       #gravity ofSaturn with units [m/s^2]
G = 6.674*pow(10, -11)          #gravitational constant with units [m^3 kg^-1 s^-2]

# Generating random particle in a box 
x = [random.randint(1, 50) for n in range(200)]
y = [random.randint(1, 50) for n in range(200)]




plt.scatter(x,y, color = 'red')
plt.show()

