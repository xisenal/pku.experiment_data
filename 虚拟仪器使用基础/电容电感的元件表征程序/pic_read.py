import numpy as np
import matplotlib.pyplot as plt

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

plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.plot(a,b)
plt.xlabel("f/Hz")
plt.ylabel("C(F) or L(H)")
plt.title("C or L-f")
plt.subplot(2,2,2)
plt.plot(a,c)
plt.xlabel("f/Hz")
plt.ylabel("R/Ohm")
plt.title("R-f")
plt.subplot(2,2,3)
plt.plot(a,d)
plt.xlabel("f/Hz")
plt.ylabel("Z/Ohm")
plt.title("Z-f")
plt.subplot(2,2,4)
plt.plot(a,e)
plt.xlabel("f/Hz")
plt.ylabel("Phase(degree)")
plt.title("Phase(degree)-f")
plt.show()