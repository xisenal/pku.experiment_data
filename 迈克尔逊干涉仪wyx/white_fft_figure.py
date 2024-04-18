import numpy as np
import matplotlib.pyplot as plt

a=[]
with open('W1.txt','r',encoding='utf-8') as file:
    for line in file:
        a.append(eval(line))

aff=np.fft.fft(a)
aff=np.fft.fftshift(aff)
aff=abs(aff)/10000
f=np.arange(1,len(a)+1)
I=np.array([1]*len(f))
f=f*0.5-772.5*I
plt.plot(f[1570:1700],aff[1570:1700])
plt.xlabel("f/10^13")
plt.ylabel("A(k^2)")
#plt.plot(f,a)
plt.show()