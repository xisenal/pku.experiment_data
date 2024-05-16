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

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题
C_list=C_list*1e6
max_valf=np.array(max_valf)
min_valf=np.array(min_valf)
vlf=min_valf-max_valf
plt.plot(C_list,vlf)
plt.xlabel(r'C/$\mu$F')
plt.ylabel(r'$f_{min}-f_{max}$/Hz')
plt.title('耦合电容C对于fano峰宽度的影响')
plt.show()