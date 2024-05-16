import numpy as np
import matplotlib.pyplot as plt

names=['0.1uF','0.2uF','0.3uF','0.4uF','0.5uF','0.6uF','0.7uF','0.8uF','0.9uF','1uF']
plt.figure(figsize=(3*7,4*7))
plt.subplots_adjust(wspace=0.5, hspace=0.5)
for i,name in enumerate(names):
    a=[]
    b=[]
    with open(name+'.txt','r',encoding='utf-8') as file:
        for line in file:
            a.append(eval(line[:8]))
            b.append(eval(line[27:35]))
    plt.subplot(3,4,i+1)
    plt.plot(a,b)
    plt.xlabel("f/Hz")
    plt.ylabel("I/UX(A/V)")
    plt.title(f"C={name}")
plt.show()