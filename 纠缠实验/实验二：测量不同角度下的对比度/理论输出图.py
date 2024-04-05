import numpy as np
import matplotlib.pyplot as plt

def draw_a_3D_surface():
    theta1=np.linspace(0,2*np.pi,1000)
    theta2=np.linspace(0,2*np.pi,1000)
    theta1_grid,theta2_grid=np.meshgrid(theta1,theta2)
    z_grid = np.empty_like(theta1_grid, dtype=float)
    for i,num1 in enumerate(theta1):
        for j,num2 in enumerate(theta2):
            z_grid[i,j]=1000*(np.sin(num1+num2))**2
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(theta1_grid, theta2_grid, z_grid, cmap='viridis')
    ax.set_xlabel('theta_1')
    ax.set_ylabel('theta_2')
    plt.show()

def draw_relative_plot(theta1):
    x=np.linspace(0,2*np.pi,10000)
    I=np.array([1]*10000)
    y=1000*(np.sin(theta1*I+x))**2
    plt.plot(x,y)
    plt.xlabel('theta2/rad')
    plt.ylabel('relative value of N')
    plt.title(f'plot for experiment when theta1={theta1}')

draw_a_3D_surface()
draw_relative_plot(0)