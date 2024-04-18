import numpy as np
import matplotlib.pyplot as plt

a=[]
with open('Hg1.txt','r',encoding='utf-8') as file:
    for line in file:
        a.append(eval(line))

aff=np.fft.fft(a)
aff=np.fft.fftshift(aff)
aff=abs(aff)/100000
f=np.arange(1,len(a)+1)
I=np.array([1]*len(f))
f=0.0125*f-98.4625*I
plt.plot(f[8205:8400],aff[8205:8400])
plt.xlabel("f/10^14")
plt.ylabel("A(k^2)")
plt.show()