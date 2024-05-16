import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op

#Fano共振按照理论公式的推导进行的研究
#记录参数：
R1=500
R2=0
L1=18e-3
L2=16e-3
C1=0.05e-6
C2=0.2e-6
C_list=np.linspace(0.01,1,100)*1e-6
min_value=[]
min_valf=[]
max_value=[]
max_valf=[]
Mval=[]
Mf=[]
for C in C_list:
    def fA(x):
        ret=R1+R2/(((x*C)**2)*((R2**2)+(x*L2-1/(x*C2)-1/(x*C))**2))
        return ret
    def fB(x):
        ret=x*L1-1/(x*C1)-1/(x*C)+(1/(x*C2)+1/(x*C)-x*L2)/(((x*C)**2)*((R2**2)+(x*L2-1/(x*C2)-1/(x*C))**2))
        return ret
    def func(f):
        ret=1/np.sqrt(fA(2*np.pi*f)**2+fB(2*np.pi*f)**2)
        return ret
    def func_neg(f):
        ret=1/np.sqrt(fA(2*np.pi*f)**2+fB(2*np.pi*f)**2)
        return -ret
    f=np.linspace(2500,5000,10000)
    y1=func(f)
    max_value.append(max(y1))
    max_valf.append(f[np.argmax(y1)])
    f=np.linspace(2500,5500,10000)
    y1=func(f)
    min_value.append(min(y1))
    min_valf.append(f[np.argmin(y1)])
    f=np.linspace(5000,10000,10000)
    y1=func(f)
    Mval.append(max(y1))
    Mf.append(f[np.argmax(y1)])

C_list=C_list*1e6
plt.figure(figsize=(2*5,3*5))
plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.subplot(3,2,1)
plt.plot(C_list,min_value)
plt.xlabel(r'C/$\mu$F')
plt.ylabel('I/UX\'s first max value/(A/V)')
plt.subplot(3,2,2)
plt.plot(C_list,min_valf)
plt.xlabel(r'C/$\mu$F')
plt.ylabel('f/Hz')
plt.subplot(3,2,3)
plt.plot(C_list,max_value)
plt.xlabel(r'C/$\mu$F')
plt.ylabel('I/UX\'s first mini value/(A/V)')
plt.subplot(3,2,4)
plt.plot(C_list,max_valf)
plt.xlabel(r'C/$\mu$F')
plt.ylabel('f/Hz')
plt.subplot(3,2,5)
plt.plot(C_list,Mval)
plt.xlabel(r'C/$\mu$F')
plt.ylabel('I/UX\'s second max value/(A/V)')
plt.subplot(3,2,6)
plt.plot(C_list,Mf)
plt.xlabel(r'C/$\mu$F')
plt.ylabel('f/Hz')
plt.show()