import numpy as np
import matplotlib.pyplot as plt

a=4.7
x=np.linspace(0,1,10000)
def f1(x):
    return (x**2)*np.exp(-a*x**2)
def f2(x):
    return ((1-x)**2)*np.exp(-a*(1-x)**2)
plt.plot(x,f1(x))
plt.plot(x,f2(x))
plt.show()