import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

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
ys=np.array(ys)
ys=abs(ys)
fig, ax1 = plt.subplots()
line1, = ax1.plot(xs, ys, 'b-', label='Theoretical value')
ax1.set_xlabel('Relative position coordinates')
ax1.set_ylabel('Relative strength', color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax2 = ax1.twinx()
line2, = ax2.plot(xs, ys/50, 'm--', label='Corresponding value')
ax2.set_ylabel('Relative strength', color='m')
ax2.tick_params(axis='y', labelcolor='m')
ax3 = ax1.twinx()
xx=[0.16,0.32,0.48,0.64,0.80,0.96,1.12,1.27,1.44,1.60,1.75,1.92,2.08,2.24,2.40,2.56,2.72,2.88,3.04,3.20]
yy=[0.03,0.05,0.07,0.10,0.11,0.04,0.11,0.25,0.38,0.49,0.58,0.37,0.40,1.17,1.89,2.52,3.02,2.71,1.07,5.28]
yerr=[0.01,0.01,0.02,0.02,0.07,0.02,0.05,0.08,0.1,0.1,0.1,0.1,0.1,0.5,0.6,0.8,0.9,0.4,0.3,0.7]
ax3.spines['right'].set_position(('outward', 60))  
line3, caplines, barlinecols= ax3.errorbar(xx,yy,yerr=yerr,fmt='o--',color="r",markersize=4, ecolor='r', capsize=4, elinewidth=1, capthick=1,label='experiment value')
ax3.set_ylabel('Relative strength', color='r')
ax3.tick_params(axis='y', labelcolor='r')
errorbar_line = mlines.Line2D([], [], color='r', marker='o', linestyle='--', label='experiment value')
lines = [line1, line2, errorbar_line]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc='upper left')
fig.tight_layout()
plt.show()
