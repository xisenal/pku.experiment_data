#深夜debug不易啊QAQ
#先使用降解法将微分方程转化为三元一阶微分方程组，再使用RK4方法执行运算这个方程组，试图解出方程的数值解
import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange

#设置全局变量
g=9.8
#设置RK4运算属性：
z=np.linspace(0,0.25,10000)
print(z)
h=z[1]-z[0]
#三个一阶函数对应方程定义(u表示y,v表示y',w表示y")
def f1(u,v,w):
    return v
def f2(u,v,w):
    return w
def f3(u,v,w):
    return -(1/(3*u*u*u))*(12*u*(v**3)+21*(u**2)*v*w+12*g*(v**2)+6*g*u*w)
#赋初值：
u=[1]
v=[-1]
w=[18.2]
#开始RK4运算：
for i in trange(1,len(z)):
    k11=f1(u[i-1],v[i-1],w[i-1])
    k12=f2(u[i-1],v[i-1],w[i-1])
    k13=f3(u[i-1],v[i-1],w[i-1])

    k21=f1(u[i-1]+k11*h/2,v[i-1]+k12*h/2,w[i-1]+k13*h/2)
    k22=f2(u[i-1]+k11*h/2,v[i-1]+k12*h/2,w[i-1]+k13*h/2)
    k23=f3(u[i-1]+k11*h/2,v[i-1]+k12*h/2,w[i-1]+k13*h/2)

    k31=f1(u[i-1]+k21*h/2,v[i-1]+k22*h/2,w[i-1]+k23*h/2)
    k32=f2(u[i-1]+k21*h/2,v[i-1]+k22*h/2,w[i-1]+k23*h/2)
    k33=f3(u[i-1]+k21*h/2,v[i-1]+k22*h/2,w[i-1]+k23*h/2)

    k41=f1(u[i-1]+k31*h,v[i-1]+k32*h,w[i-1]+k33*h)
    k42=f2(u[i-1]+k31*h,v[i-1]+k32*h,w[i-1]+k33*h)
    k43=f3(u[i-1]+k31*h,v[i-1]+k32*h,w[i-1]+k33*h)

    u.append(u[i-1]+h*(k11+2*k21+2*k31+k41)/6)
    v.append(v[i-1]+h*(k12+2*k22+2*k32+k42)/6)
    w.append(w[i-1]+h*(k13+2*k23+2*k33+k43)/6)

plt.plot(z,u)
plt.show()