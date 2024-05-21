import numpy as np
import matplotlib.pyplot as plt
import data_read as dr

y1,y2=dr.read_tri()
t=dr.imp_t()
X1 = np.fft.fft(y1)
X2 = np.fft.fft(y2)
X1[0]=0
X2[0]=0
freqs = np.fft.fftfreq(len(t), t[1] - t[0])
idx0 = np.argmax(np.abs(X1))
f1=freqs[idx0]
idx = np.argmax(np.abs(X2))
f22=freqs[idx]
f2=freqs[idx0]

import numpy as np
from scipy.optimize import leastsq
def sin_func(x, A, phi, C, f):
    return A * np.sin(2 * np.pi * f * x + phi) + C
def residuals(params, x, y, f):
    A, phi, C = params
    return y - sin_func(x, A, phi, C, f)

x_data = np.array(t) 
y_data = np.array(y2) 
f = f2
initial_guess = [1, 0, 0]  # 振幅、相位和偏置的初始猜测
result = leastsq(residuals, initial_guess, args=(x_data, y_data, f))
A_fit, phi_fit, C_fit = result[0]


f = f22
initial_guess = [1, 0, 0]  # 振幅、相位和偏置的初始猜测
result = leastsq(residuals, initial_guess, args=(x_data, y_data, f))
A_fit1, phi_fit1, C_fit1 = result[0]

print(f"拟合振幅 A: {A_fit}")
print(f"拟合相位 phi: {phi_fit}")
print(f"拟合偏置 C: {C_fit}")
x=t
plt.plot(t,y2,'b-',label='origin data')
plt.plot(x,A_fit*np.sin(2*np.pi*f2*x+phi_fit)+C_fit,'r--',label='fitting value f=10Hz')
plt.plot(x,A_fit1*np.sin(2*np.pi*f22*x+phi_fit1)+C_fit1,'r--',label='fitting value f=20Hz')
plt.legend(loc='upper right')
plt.show()