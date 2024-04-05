import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def f1(x, a):
    return (x**2) * np.exp(-a * x**2)
def f2(x, a):
    return ((1 - x)**2) * np.exp(-a * (1 - x)**2)
def f3(x, a):
    return f1(x, a) - f2(x, a)
a = np.linspace(3, 5.5, 1000)
find1 = []
find2 = []
for i in a:
    x = fsolve(f3, 0.25, args=(i,))
    find1.append(x[0])
    x = fsolve(f3, 0.75, args=(i,))
    find2.append(x[0])
find=[0.5]*len(a)
for i in range(1000):
    if abs(find1[i]-find2[i])>1e-5:
        print(a[i])
        break
plt.plot(a, find1, label='smaller values')
plt.plot(a, find2, label='bigger values')
plt.plot(a,find,label='middle values')
plt.xlabel('a')
plt.ylabel('n_R or n_L')
plt.title('Symmetric and Asymmetric Solutions')
plt.legend()
plt.show()