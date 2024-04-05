#波形计算方法：
import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange

def T_mesh(p):
   A=np.array([[np.cos(p),np.sin(p)],[-np.sin(p),np.cos(p)]])
   return A

#设置参数：
tau=0.33
m_b=0.106*10**(-3)
mu_0=0.000549
a_num=0.2
ita=m_b/(mu_0*a_num)
F_T=8.93
N=6
#设置求解频率：
pop=np.sqrt(F_T/(mu_0*a_num**2))/(2*np.pi)
omega=187.28
delta=omega/pop
#设置对应条件的M矩阵
M=np.array([[1,0],[-ita*delta,1]])
#设置求解长度范围
x=np.linspace(-tau,N-tau,100000)
y=[0]
#求解x位置上的y值
def solve_y(w):
   phi=np.array([0,1])
   phi=phi.T
   if w<0:
      phix=T_mesh(delta*(w+tau))@phi
      return phix
   elif 0<=w<1:
      phix=T_mesh(delta*w)@M@T_mesh(delta*tau)@phi
      return phix
   else:
      phi_x=solve_y(w-1)
      phiarr=np.array(phi_x)
      phiarr=phiarr.T
      phix=T_mesh(delta*(w-np.floor(w)))@M@T_mesh(delta*(np.floor(w)-w+1))@phiarr
      return phix

arri=np.arange(1,100000)
for i in arri:
   phi_arr=solve_y(x[i])
   y.append(phi_arr[0])

   

for i in arri:
   if y[i-1]*y[i]<0:
      print(x[i])

y1=[-a for a in y]
xp=x[:]
yp=y[:]
y1p=y1[:]
plt.plot(xp, yp)
plt.plot(xp, y1p)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('wave of N=6,t=0.33')
plt.show()