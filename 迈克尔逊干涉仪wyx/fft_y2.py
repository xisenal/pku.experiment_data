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

y1=np.array(y1[5000:-2000])
y2=np.array(y2)
Y1=np.fft.fft(y2)
Y1=abs(np.fft.fftshift(Y1))
f=np.arange(1,len(y2)+1)
plt.plot(f,Y1)
plt.show()