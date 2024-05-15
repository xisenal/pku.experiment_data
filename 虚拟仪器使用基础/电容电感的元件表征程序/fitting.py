import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

a=[]
b=[]
c=[]
d=[]
e=[]
name=input("输入文件名称：")
name=name+'.txt'
with open(name,'r',encoding='utf-8') as file:
    for line in file:
        a.append(eval(line[:8]))
        b.append(eval(line[9:17]))
        c.append(eval(line[18:26]))
        d.append(eval(line[27:35]))
        e.append(eval(line[36:45]))

d=np.array(d)
c=np.array(c)
a=np.array(a)
X=a**2
Y=c**2
slope, intercept, r_value, p_value, std_err = st.linregress(a, d)
print("通过阻抗进行拟合：")
print(slope,intercept,r_value)
print(f"L={1000*slope/(2*np.pi)}mH")
slope, intercept, r_value, p_value, std_err = st.linregress(X, Y)
print("对于损耗电阻的拟合：")
print(slope,intercept,r_value)
R=np.sqrt(Y+X*4*(np.pi**2)*(0.016)**2)
print(R)
slope, intercept, r_value, p_value, std_err = st.linregress(a, R)
print("损耗电阻随频率的变化：")
print(slope,intercept,r_value)
plt.plot(a,R)
plt.show()