#debug的最终结局就是觉得啥都不对
import numpy as np
import matplotlib.pyplot as plt
import cmath
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tqdm import trange
import time
#相关参数
Num=128
V_0=0.45
OmeR=8
Omer=5
dbetRr=5
N_index=1000
dt=0.1
timeround=10000
#定义两个平面坐标
x=np.linspace(-30,30,Num)
y=np.linspace(-30,30,Num)
dx=x[1]-x[0]
dy=y[1]-y[0]
#构建两个坐标对应的矩阵空间
X,Y=np.meshgrid(x,y)
#定义两个频域坐标：
kx=np.linspace(-np.pi/dx,np.pi/dx,Num)
ky=np.linspace(-np.pi/dy,np.pi/dy,Num)
KX,KY=np.meshgrid(kx,ky)
#构建势能\P的空间矩阵\Fourier变换后的特解矩阵
V_2ff=-V_0*np.exp(-((X**2+Y**2)/OmeR**2)**N_index)*(1-np.exp(-((X**2+Y**2)/Omer**2)**N_index))-V_0*np.exp(-((X**2+Y**2)/(2*OmeR+dbetRr-Omer)**2)**N_index)*(1-np.exp(-((X**2+Y**2)/(dbetRr+OmeR)**2)**N_index))
P_func=1.1*np.exp(-(X**2+Y**2)/2500)
Four_result=np.exp(-0.5788j*(KX**2+KY**2)*dt)
"""
#画一下势能图：
fig = plt.figure()
ax = fig.add_subplot(211)
im = ax.pcolormesh(X, Y, V_try, cmap='viridis') 
ax.set_title('6')
ax.set_xlabel('x')
ax.set_ylabel('y')
fig.colorbar(im, ax=ax) 
plt.show()
"""
#定义两个可以运算的矩阵用于迭代和储存数据并赋予初始值
Psi=np.exp(1j*np.angle(X+Y*1j))/60
N=0*Psi
#进行RK4迭代：
def f1(Psi,N):
    return -0.04*Psi-0.0046j*Psi*abs(Psi)**2-0.0092j*N*Psi+0.005*N*Psi-1.52j*Psi*V_2ff
def f2(Psi,N):
    return -0.12*N-0.01*N*abs(Psi)**2+P_func
for k in trange(timeround):
    k1p=f1(Psi,N)
    k1n=f2(Psi,N)

    k2p=f1(Psi+dt*k1p/2,N+dt*k1n/2)
    k2n=f2(Psi+dt*k1p/2,N+dt*k1n/2)

    k3p=f1(Psi+dt*k2p/2,N+dt*k2n/2)
    k3n=f2(Psi+dt*k2p/2,N+dt*k2n/2)

    k4p=f1(Psi+dt*k3p,N+dt*k3n)
    k4n=f2(Psi+dt*k3p,N+dt*k3n)

    Psi=Psi+dt*(k1p+2*k2p+2*k3p+k4p)/6
    N=N+dt*(k1n+2*k2n+2*k3n+k4n)/6

    Psi=np.fft.fft2(Psi)
    Psi=np.fft.fftshift(Psi)
    Psi=Psi*Four_result
    Psi=np.fft.fftshift(Psi)
    Psi=np.fft.ifft2(Psi)

Pmo=abs(Psi)**2
Pmo=Pmo.astype(float)
"""
fig = plt.figure()
ax = fig.add_subplot(111)
im = ax.pcolormesh(X, Y, Pmo, shading='auto') 
ax.set_title('the 2D figure of |Psi|^2')
ax.set_xlabel('x')
ax.set_ylabel('y')
fig.colorbar(im, ax=ax) 
plt.show()
"""
"""
fig = plt.figure()
ax = fig.add_subplot(111)

# 绘制平面 3D 图
img = ax.imshow(Pmo, cmap='jet', interpolation='nearest')  # 使用 'jet' 颜色映射，'nearest' 插值方式
ax.set_title('3D Plot of Pmo')
ax.set_xlabel('X')
ax.set_ylabel('Y')
cbar = fig.colorbar(img)
cbar.set_label('Intensity')

# 显示图形
plt.show()
"""

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Pmo, cmap='jet', rstride=1, cstride=1)
ax.set_title('3D Plot of Pmo')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Intensity')

# 添加颜色条
fig.colorbar(surf)

# 显示图形
plt.show()