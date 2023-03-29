import math 
import numpy as np
import matplotlib.pyplot as plt 
import random 
 
# Useful values
r = 58232*pow(10, 3)            # radius of Saturn with units [m]
M = 5.683*pow(10, 26)           # mass of Saturn with units [kg]
g = 10.44                       # gravity of Saturn with units [m/s^2]
G = 6.674*pow(10, -11)          # gravitational constant with units [m^3 kg^-1 s^-2]
rho = 1000                      # density of particle in Saturn's rings with units [kg/m^3]
r_d = 500 * pow(10, -9)         # Average radius of particles with units [m]
V = 4/3 * math.pi * pow(r_d, 3) # Volume of particles 
m_p = rho / V                   # Mass of particles 

# Generating random particle in a plot
x = [random.uniform(-100, 100) for n in range(50)]
y = [random.uniform(-100, 100) for n in range(50)]

numparticles = 50

# Kepler's third law
T = math.sqrt(4 * pow(math.pi, 2) / (G * M) * pow(r, 3))

# Defining omega
Omega = 2 * math.pi / T

# Gravitational force
F_g = G * M * m_p / pow(r, 2)

# Gravitational acceleration of the particle
g_g = F_g / m_p

# Velocity for x and y directions
v_x = []
v_y = []

for j in range(len(x)):
   vx =  - 2 / 3 * Omega *  y[j]
   v_x.append(vx)
   
   vy = -g_g 
   v_y.append(vy)

# Seting the time step 
dt = 0.1

# Seting the initial momentum to zero
total_momentum = 0

# Calculating the momentum of each particle and add it to the total momentum
momenta = []
for j in range(numparticles):
    momentum = m_p * v_x[j]
    momenta.append(momentum)
    total_momentum += momentum

# Recording the time
time = 0

# Momentum over time
times = [0] # initial time
momentum_values = [total_momentum]
for i in range(100):
    # Updating the positions and velocities
    for j in range(numparticles):
        x[j] += v_x[j] * dt
        y[j] += v_y[j] * dt

    # Calculating new momentum and add it to the total momentum
    new_momenta = []
    for position in x:
        momentum = random.uniform(-1, 1)
        new_momenta.append(momentum)
        total_momentum += momentum

    # Updating the momentum of each particle to ensure conservation of momentum
    average_momentum = total_momentum / numparticles
    for j in range(numparticles):
        momenta[j] += average_momentum - new_momenta[j]

    # Updating the time
    time += dt
    times.append(time)

    # Updating the momentum_values list
    momentum_values.append(total_momentum)

# Plotting the graph 
plt.figure(figsize = (6,4))
plt.plot(times, momentum_values, color = 'purple')
plt.xlabel('Time (s)')
plt.ylabel('Total momentum (Ns)')
plt.show()