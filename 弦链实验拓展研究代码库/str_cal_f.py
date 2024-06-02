import numpy as np
import matplotlib.pyplot as plt

def T_mesh(p):
   A=np.array([[np.cos(p),np.sin(p)],[-np.sin(p),np.cos(p)]])
   return A

#设置参数：
tau=0
m_b=0.114*10**(-3)
mu_0=0.000549
a_num=0.3
mu_1=36*mu_0
F_T=8.93
N=4
f=np.linspace(0,1000,100000)
deltas1=2*np.pi*np.sqrt(mu_1*f**2*a_num**2/F_T)
deltas2=2*np.pi*np.sqrt(mu_0*f**2*a_num**2/F_T)
nope=[]
for j,fnum in enumerate(f):
   if j==0:
      continue
   delta1=deltas1[j]
   delta2=deltas2[j]
   phi=np.array([0,1])
   for i in range(N):
      phi=T_mesh(delta1*0.2)@phi
      phi[1]=phi[1]*delta1/delta2
      phi=T_mesh(delta2*(1-0.2))@phi
      phi[1]=phi[1]*delta2/delta1
   nope.append(phi[0])

# plt.plot(f[1:4001],nope[:4000])
# plt.show()


ans=[]
for i in range(len(nope)-1):
   if nope[i]*nope[i+1]<=0:
      ans.append(f[i])

for i,num in enumerate(ans):
   print(i,num)

# xlss=np.linspace(1/N,1-1/N,N-1)
# xrss=np.flip(xlss)
# plt.plot(xlss,ans[:N-1])
# plt.plot(xrss,ans[N:N*2-1])
# plt.plot(xlss,ans[N*2:N*3-1])
# plt.show()
