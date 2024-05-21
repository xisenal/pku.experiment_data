from calcu2 import freq,amp
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def func(x, F, k):
    return F/(k**2+1e-6*4*np.pi**2*x**2)
x_data = freq
y_data = amp
popt, pcov = curve_fit(func, x_data, y_data)
print("拟合参数:", popt)
y_fit = func(x_data, *popt)
plt.plot(x_data, y_data, label='Data')
plt.plot(x_data, y_fit, color='red', label='Fit')
plt.legend()
plt.show()
