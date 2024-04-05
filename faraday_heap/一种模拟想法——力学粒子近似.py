import numpy as np
import matplotlib.pyplot as plt

num_particles = 500
box_length = 50.0   
box_width = 0.5    
box_height = 10.0    
k = 0.1           
gamma = 0.05        
dt = 0.1            
total_steps = 60   
g = 9.81             

positions = np.random.uniform(low=0, high=box_length, size=num_particles)
velocities = np.zeros(num_particles)

for step in range(total_steps):
    forces = -k * positions - gamma * velocities
    forces += np.full_like(positions, g) 
    velocities += forces * dt
    positions += velocities * dt
    velocities -= np.mean(velocities)
    positions = np.clip(positions, 0, box_length)
    plt.clf()
    plt.scatter(positions, np.random.uniform(low=0, high=box_width, size=num_particles), color='blue', s=2)
    plt.title("Step {}".format(step))
    plt.xlabel("L")
    plt.ylabel("H")
    plt.xlim(0, box_length)
    plt.ylim(0, box_height)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.pause(0.01)

plt.show()
