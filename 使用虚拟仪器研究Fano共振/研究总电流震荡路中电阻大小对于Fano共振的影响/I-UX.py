import numpy as np
import matplotlib.pyplot as plt

names=['100','300','500','700','900']
for i,name in enumerate(names):
    a=[]
    b=[]
    with open(name+'Ohm'+'.txt','r',encoding='utf-8') as file:
        for line in file:
            a.append(eval(line[:8]))
            b.append(eval(line[27:35]))
    plt.plot(a,b,label=f'R={name}')
    plt.xlabel("f/Hz")
    plt.ylabel("I/UX(A/V)")
plt.legend()
plt.show()