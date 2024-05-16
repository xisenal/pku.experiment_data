import numpy as np
import matplotlib.pyplot as plt
a=[]
b=[]
with open('究极细测标准版.txt','r',encoding='utf-8') as file:
    for line in file:
        a.append(eval(line[:8]))
        b.append(eval(line[27:35]))
R1=500+50
R2=0+9
L1=(18+2)*1e-3
L2=(16+2)*1e-3
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
plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False    
plt.plot(a,b,label='实验值')
plt.plot(f,y,label='理论值')
plt.legend(loc='upper right')
plt.show()