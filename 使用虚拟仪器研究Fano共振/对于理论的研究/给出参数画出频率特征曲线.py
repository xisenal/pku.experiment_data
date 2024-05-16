import numpy as np
import matplotlib.pyplot as plt

#Fano共振按照理论公式的推导进行的研究
#记录参数：
R1=500
R2=0
L1=18e-3
L2=16e-3
C1=0.05e-6
C2=0.2e-6
C=0.5e-6
#画出此参数下的I/UX随频率变化的图像：
f=np.linspace(1000,10000,100000)
omega=2*np.pi*f
def fA(x):
    ret=R1+R2/(((x*C)**2)*((R2**2)+(x*L2-1/(x*C2)-1/(x*C))**2))
    return ret
def fB(x):
    ret=x*L1-1/(x*C1)-1/(x*C)+(1/(x*C2)+1/(x*C)-x*L2)/(((x*C)**2)*((R2**2)+(x*L2-1/(x*C2)-1/(x*C))**2))
    return ret
A=fA(omega)
B=fB(omega)
y=1/np.sqrt(A**2+B**2)
z=-np.arctan(B/A)*(180/np.pi)
plt.figure(figsize=(14,5))
plt.subplot(1,2,1)
plt.plot(f,y)
plt.xlabel('f/Hz')
plt.ylabel("I/UX(A/V)")
plt.subplot(1,2,2)
plt.plot(f,z)
plt.xlabel('f/Hz')
plt.ylabel("phase/degree")
plt.show()