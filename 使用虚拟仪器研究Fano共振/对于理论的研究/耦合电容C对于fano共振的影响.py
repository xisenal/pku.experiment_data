import numpy as np
import matplotlib.pyplot as plt

#Fano共振按照理论公式的推导进行的研究
#可变参数：
R1=500
R2=0
L1=18e-3
L2=16e-3
C1=0.05e-6
C2=0.2e-6
C_list=1e-6*np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
#画出此参数下的I/UX随频率变化的图像：
plt.figure(figsize=(21,28))
plt.subplots_adjust(wspace=0.5, hspace=0.5)
for i,C in enumerate(C_list):
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
    plt.subplot(3,4,i+1)    
    plt.plot(f,y) 
    plt.xlabel('f/Hz')
    plt.ylabel("I/UX(A/V)") 
plt.show()