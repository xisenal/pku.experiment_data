import numpy as np
import matplotlib.pyplot as plt

theta1 = np.linspace(0, 2 * np.pi, 128)
theta2 = np.linspace(0, 2 * np.pi, 128)
theta1_grid, theta2_grid = np.meshgrid(theta1, theta2)
def Q_sq(x, y):
    return np.kron(np.array([[np.cos(2 * x), np.sin(2 * x)], [-np.sin(2 * x), np.cos(2 * x)]]),
                   np.array([[np.cos(2 * y), np.sin(2 * y)], [-np.sin(2 * y), np.cos(2 * y)]]))
psi = np.sqrt(1 / 2) * np.array([[0], [1], [1], [0]])
z_grid = np.empty_like(theta1_grid, dtype=float)
for i in range(len(theta1)):
    for j in range(len(theta2)):
        z_grid[i, j] = (psi.T @ Q_sq(theta1_grid[i, j], theta2_grid[i, j]) @ psi).item()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(theta1_grid, theta2_grid, z_grid, cmap='viridis')
ax.set_xlabel('theta_1')
ax.set_ylabel('theta_2')
ax.set_zlabel('E_exp')
plt.show()