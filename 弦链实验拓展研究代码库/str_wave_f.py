import numpy as np
import matplotlib.pyplot as plt

def T_mesh(p):
   A=np.array([[np.cos(p),np.sin(p)],[-np.sin(p),np.cos(p)]])
   return A

#设置参数：
mu_0=0.000549
a_num=0.3
mu_1=36*mu_0
F_T=8.93
N=4
f=93.2909329093291
delta1=2*np.pi*np.sqrt(mu_0*f**2*a_num**2/F_T)
delta2=2*np.pi*np.sqrt(mu_1*f**2*a_num**2/F_T)
xs=np.linspace(0,N,100000)
ys=np.linspace(0,N,100000)
for i,x in enumerate(ys):
   if x>=0 and x<0.8:
      phi=np.array([0,1])
      dl=T_mesh(delta1*x)@phi
      ys[i]=dl[0]
   elif x>=0.8 and x<1:
      phi=np.array([0,1])
      dl=T_mesh(delta1*0.8)@phi
      dl[1]=dl[1]*delta1/delta2
      dl=T_mesh(delta2*(x-0.8))@dl
      ys[i]=dl[0]
   elif x>=1 and x<1.8:
      phi=np.array([0,1])
      phi=T_mesh(delta1*0.8)@phi
      phi[1]=phi[1]*delta1/delta2
      phi=T_mesh(delta2*0.2)@phi
      phi[1]=phi[1]*delta2/delta1
      dl=T_mesh(delta1*(x-1))@phi
      ys[i]=dl[0]
   elif x>=1.8 and x<2:
      phi=np.array([0,1])
      phi=T_mesh(delta1*0.8)@phi
      phi[1]=phi[1]*delta1/delta2
      phi=T_mesh(delta2*0.2)@phi
      phi[1]=phi[1]*delta2/delta1
      phi=T_mesh(delta1*0.8)@phi
      phi[1]=phi[1]*delta1/delta2
      dl=T_mesh(delta2*(x-1.8))@phi
      ys[i]=dl[0]
   elif x>=2 and x<2.8:
      phi=np.array([0,1])
      phi=T_mesh(delta1*0.8)@phi
      phi[1]=phi[1]*delta1/delta2
      phi=T_mesh(delta2*0.2)@phi
      phi[1]=phi[1]*delta2/delta1
      phi=T_mesh(delta1*0.8)@phi
      phi[1]=phi[1]*delta1/delta2
      phi=T_mesh(delta2*0.2)@phi
      phi[1]=phi[1]*delta2/delta1
      dl=T_mesh(delta1*(x-2))@phi
      ys[i]=dl[0]
   elif x>=2.8 and x<3:
      phi=np.array([0,1])
      phi=T_mesh(delta1*0.8)@phi
      phi[1]=phi[1]*delta1/delta2
      phi=T_mesh(delta2*0.2)@phi
      phi[1]=phi[1]*delta2/delta1
      phi=T_mesh(delta1*0.8)@phi
      phi[1]=phi[1]*delta1/delta2
      phi=T_mesh(delta2*0.2)@phi
      phi[1]=phi[1]*delta2/delta1
      phi=T_mesh(delta1*0.8)@phi
      phi[1]=phi[1]*delta1/delta2
      dl=T_mesh(delta2*(x-2.8))@phi
      ys[i]=dl[0]
   elif x>=3 and x<3.8:
      phi=np.array([0,1])
      phi=T_mesh(delta1*0.8)@phi
      phi[1]=phi[1]*delta1/delta2
      phi=T_mesh(delta2*0.2)@phi
      phi[1]=phi[1]*delta2/delta1
      phi=T_mesh(delta1*0.8)@phi
      phi[1]=phi[1]*delta1/delta2
      phi=T_mesh(delta2*0.2)@phi
      phi[1]=phi[1]*delta2/delta1
      phi=T_mesh(delta1*0.8)@phi
      phi[1]=phi[1]*delta1/delta2
      phi=T_mesh(delta2*0.2)@phi
      phi[1]=phi[1]*delta2/delta1
      dl=T_mesh(delta1*(x-3))@phi
      ys[i]=dl[0]
   elif x>=3.8 and x<4:
      phi=np.array([0,1])
      phi=T_mesh(delta1*0.8)@phi
      phi[1]=phi[1]*delta1/delta2
      phi=T_mesh(delta2*0.2)@phi
      phi[1]=phi[1]*delta2/delta1
      phi=T_mesh(delta1*0.8)@phi
      phi[1]=phi[1]*delta1/delta2
      phi=T_mesh(delta2*0.2)@phi
      phi[1]=phi[1]*delta2/delta1
      phi=T_mesh(delta1*0.8)@phi
      phi[1]=phi[1]*delta1/delta2
      phi=T_mesh(delta2*0.2)@phi
      phi[1]=phi[1]*delta2/delta1
      phi=T_mesh(delta1*0.8)@phi
      phi[1]=phi[1]*delta1/delta2
      dl=T_mesh(delta2*(x-3.8))@phi
      ys[i]=dl[0]
else:
      phi=np.array([0,1])
      phi=T_mesh(delta1*0.8)@phi
      phi[1]=phi[1]*delta1/delta2
      phi=T_mesh(delta2*0.2)@phi
      phi[1]=phi[1]*delta2/delta1
      phi=T_mesh(delta1*0.8)@phi
      phi[1]=phi[1]*delta1/delta2
      phi=T_mesh(delta2*0.2)@phi
      phi[1]=phi[1]*delta2/delta1
      phi=T_mesh(delta1*0.8)@phi
      phi[1]=phi[1]*delta1/delta2
      phi=T_mesh(delta2*0.2)@phi
      phi[1]=phi[1]*delta2/delta1
      phi=T_mesh(delta1*0.8)@phi
      phi[1]=phi[1]*delta1/delta2
      phi=T_mesh(delta2*0.2)@phi
      phi[1]=phi[1]*delta2/delta1
      ys[i]=phi[0]

ans=[]
for i in range(len(ys)-1):
   if ys[i]*ys[i+1]<=0:
      ans.append(xs[i])

print(ans+[4.0])

ys=np.array(ys)


plt.plot(xs,abs(ys),color='r')
# plt.plot(xs,-abs(ys),color='r')
plt.title("Waveform diagram under PhC algorithm")
plt.xlabel("Relative position coordinates")
plt.ylabel("Relative strength")
plt.show()