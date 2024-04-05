import numpy as np
import matplotlib.pyplot as plt

num_small_particles = 1000
num_large_particles = 1
small_particle_diameter = 0.05  
large_particle_diameter = 1.5  
container_width = 5.0
container_length = 2.0
container_height = 15.0
small_particles_height = 6.0
vibration_frequency = 40.0  
amplitude_range = np.linspace(0.01, 0.5, 50) 
dt = 0.01  
num_steps = 1000
small_particles_y = np.random.uniform(small_particle_diameter / 2, small_particles_height - small_particle_diameter / 2, num_small_particles)
small_particles_x = np.random.uniform(small_particle_diameter / 2, container_width - small_particle_diameter / 2, num_small_particles)
small_particles_vy = np.zeros(num_small_particles)
large_particle_y = container_height - large_particle_diameter / 2
large_particle_x = container_width / 2.0
large_particle_vy = 0.0
rise_velocities = []
for amplitude in amplitude_range:
    small_particles_y = np.random.uniform(small_particle_diameter / 2, small_particles_height - small_particle_diameter / 2, num_small_particles)
    large_particle_y = container_height - large_particle_diameter / 2
    for step in range(num_steps):
        t = step * dt
        vibration = amplitude * np.sin(2 * np.pi * vibration_frequency * t)
        small_particles_vy += vibration    
        small_particles_y += small_particles_vy * dt
        hit_top = small_particles_y + small_particle_diameter / 2 > container_height
        small_particles_y[hit_top] = container_height - small_particle_diameter / 2
        small_particles_vy[hit_top] *= -0.9 
        hit_bottom = small_particles_y - small_particle_diameter / 2 < 0
        small_particles_y[hit_bottom] = small_particle_diameter / 2
        small_particles_vy[hit_bottom] *= -0.9 
        if large_particle_y <= container_height:
            large_particle_vy += 0.1 
            large_particle_y += large_particle_vy * dt
        else:
            rise_velocities.append(large_particle_vy) 
            break
rise_velocities=np.array(rise_velocities)
I=np.array([1]*len(rise_velocities))
times=small_particles_height*I/rise_velocities
plt.figure(figsize=(10, 6))
plt.plot(np.log(amplitude_range), np.log(times), marker='.', linestyle='-')
plt.xlabel('Amplitude (A)')
plt.ylabel('Rise Time of Large Particle (s)')
plt.title('Rise Time of Large Particle vs. Amplitude')
plt.grid(True)
plt.show()