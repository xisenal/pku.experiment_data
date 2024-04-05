import numpy as np
import matplotlib.pyplot as plt

a=[0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180]
b=[50,80,124,140,144,123,83,64,61,52,113,166,201,210,141,119,77,57,52]
c=[2800,2754,2692,2693,2695,2691,2688,2646,2589,2558,2487,2285,2224,2131,2245,2284,2319,2430,2761]
a=np.array(a)
b=np.array(b)
c=np.array(c)
A=c/b
plt.plot(a,A,marker='*', markersize=6, color='b')
plt.xlabel('angel/degree')
plt.ylabel('contrast ratio')
plt.title('experiment result')
plt.show()