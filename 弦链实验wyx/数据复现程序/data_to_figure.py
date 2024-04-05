import numpy as np
from matplotlib import pyplot as plt

with open('程序读取数据.txt',encoding='utf-8') as file:
     content=file.read()
data=[]
dat=""
for line in content:
    if line=="\n":
        data.append(dat)
        dat=""
    else:
        dat+=line
        
x=[]
y=[]
for i in data:
    i=i.split("  -")
    freq=i[0][2:]
    inte=i[1][:-1]
    n=int(freq[-1])
    x.append(float(freq[:-4])*(10**n))
    n=int(inte[-1])
    y.append(float(inte[:-4])*(10**n))
    
x=np.array(x)
y=np.array(y)
y=-1*y
print(y)
fig = plt.figure(figsize=(8, 6))
plt.plot(x, y, color="blue")
plt.show()
