import matplotlib.pyplot as plt
import numpy as np

y1=[]
y2=[]
with open('wyxhg1.txt','r',encoding='utf-8') as file:
    for line in file:
        if line[0]=='D':
            continue
        else:
            y1.append(eval(line[21:28]))
            y2.append(eval(line[33:40]))
            
y1=np.array(y1)*(10**(-4))
y2=np.array(y2)*(10**(-5))
length=len(y1)
t=np.arange(1,length+1)
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(t,y1)
plt.subplot(1,2,2)
plt.plot(t,y2)
plt.show()