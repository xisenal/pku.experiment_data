#有关杂质态的计算
import numpy as np
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
I=np.array([[1,0],[0,1]])

#设置求解区间：
delta=np.linspace(0,10,100000)
nope=[]
ans=[]
for i in trange(100000):
   delta_num=delta[i]
   phi=np.array([0,1])
   phi=phi.T
   M=np.array([[1,0],[-ita*delta_num,1]])
   phi=T_mesh(delta_num*(1-tau))@M@T_mesh(delta_num*tau)@phi
   phi=T_mesh(delta_num*(2-tau-np.floor(2-tau)))@I@T_mesh(delta_num*(np.floor(2-tau)-2+tau+1))@phi
   phi=T_mesh(delta_num*(3-tau-np.floor(3-tau)))@M@T_mesh(delta_num*(np.floor(3-tau)-3+tau+1))@phi
   phi=T_mesh(delta_num*(4-tau-np.floor(4-tau)))@M@T_mesh(delta_num*(np.floor(4-tau)-4+tau+1))@phi
   phi=T_mesh(delta_num*(5-tau-np.floor(5-tau)))@M@T_mesh(delta_num*(np.floor(5-tau)-5+tau+1))@phi
   phi=T_mesh(delta_num*(6-tau-np.floor(6-tau)))@M@T_mesh(delta_num*(np.floor(6-tau)-6+tau+1))@phi
#   phi=T_mesh(delta_num*(7-tau-np.floor(7-tau)))@M@T_mesh(delta_num*(np.floor(7-tau)-7+tau+1))@phi
   nope.append(abs(phi[0]))

range_by=np.arange(1,100000-1)
for i in range_by:
    if nope[i-1]>nope[i] and nope[i]<nope[i+1]:
        ans.append(delta[i])
pop=np.sqrt(F_T/(mu_0*a_num**2))/(2*np.pi)
for i in range(len(ans)):
   ans[i]=ans[i]*pop
print(ans)