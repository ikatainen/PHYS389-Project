import math 
import numpy as np
import matplotlib.pyplot as plt 
 

#Useful values
r = 58232*pow(10, 3)            #radius of Saturn with units [m]
M = 5.683*pow(10, 26)           #mass of Saturn with units [kg]
g = 10.44                       #gravity ofSaturn with units [m/s^2]
G = 6.674*pow(10, -11)          #gravitational constant with units [m^3 kg^-1 s^-2]

# Defining velocity, position and mass
 def Rings(, x, m):
    self.v = v
    self.x = x
    self.m = m

#Keplers third law for period T
T = ((4* math.pi**2)/(G*M)*r**3)**(0.5)

#Plotting a graph to show the points 

plt.scatter(r, M)

plt.show()