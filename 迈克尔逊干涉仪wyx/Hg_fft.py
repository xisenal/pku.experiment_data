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

y1=np.array(y1)
y2=np.array(y2)

print(len(y1))
Cons=np.mean(y1)
I=np.array([1]*len(y1))
Y1=(Cons*I-y1)/Cons
Y1=y2
Y1_fft=np.fft.fft(Y1)
Y1_fft=abs(np.fft.fftshift(Y1_fft))
f=np.arange(1,len(Y1_fft)+1)
print(len(f))
plt.plot(f,Y1_fft)
plt.show()