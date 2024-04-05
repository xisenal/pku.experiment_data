import numpy as np
import matplotlib.pyplot as plt

#设置参数：
mu_0=0.000549
m_b=0.106*10**(-3)
a_num=0.2
F_T=9.01

fx=np.linspace(0,1000,100000)
fx=np.array(fx)
f1=np.cos(np.sqrt(mu_0/F_T)*2*np.pi*a_num*fx)-((m_b*2*np.pi*fx)/(2*F_T))*np.sqrt(F_T/mu_0)*np.sin(np.sqrt(mu_0/F_T)*2*np.pi*a_num*fx)
f2=np.ones(100000)
f3=[-x for x in f2]
plt.plot(fx,f1)
plt.plot(fx,f2)
plt.plot(fx,f3)
plt.show()