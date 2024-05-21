import numpy as np
from scipy.optimize import curve_fit
import pic_read as pr
import matplotlib.pyplot as plt

t1=pr.t1
t2=pr.t2
x1=pr.x1
x2=pr.x2

# def sine_function(x, A, omega, phi, offset):
#     return A * np.sin(omega * x + phi) + offset

# params_y1, _ = curve_fit(sine_function, t1, x1, p0=[1, 1, 0, 0])
# params_y2, _ = curve_fit(sine_function, t2, x2, p0=[1, 1, 0, 0])

# phi_y1 = params_y1[2]
# phi_y2 = params_y2[2]

# phase_difference = phi_y2 - phi_y1
# phase_difference = (phase_difference + np.pi) % (2 * np.pi) - np.pi
# print("相位差:", phase_difference)

# x=t1
# y1=params_y1[0] * np.sin(params_y1[1] * x + params_y1[2]) + params_y1[3]
# y2=params_y2[0] * np.sin(params_y2[1] * x + params_y2[2]) + params_y2[3]

# plt.plot(t1,x1,'b')
# # plt.plot(t2,x2,'b')
# plt.plot(x,y1,'r--')
# # plt.plot(x,y2,'r--')
# plt.show()


#使用傅里叶变换的方法似乎比scipy中的拟合准确度更高！
X1 = np.fft.fft(x1)
X2 = np.fft.fft(x2)
X1[0]=0
X2[0]=0
freqs = np.fft.fftfreq(len(t1), t1[1] - t1[0])
idx = np.argmax(np.abs(X1))
phase_x1 = np.angle(X1[idx])
f1=freqs[idx]
idx = np.argmax(np.abs(X2))
phase_x2 = np.angle(X2[idx])
f2=freqs[idx]
phase_difference = phase_x2 - phase_x1
phase_difference = (phase_difference + np.pi) % (2 * np.pi) - np.pi
x=t1

if __name__=="__main__":
    print("相位差:", phase_difference)
    plt.plot(t1,x1,'b',label='original pic')
    plt.plot(t2,x2,'b')
    plt.plot(x,120*np.sin(2*np.pi*f1*x+phase_x1)-267,'r--',label='fitting pic')
    plt.plot(x,22*np.sin(2*np.pi*f2*x+phase_x2)-290,'r--')
    plt.legend(loc='upper right')
    plt.show()
