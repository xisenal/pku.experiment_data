import numpy as np
import matplotlib.pyplot as plt
import data_read as dr
from pprint import pprint

y1,y2=dr.read_single()
t=dr.imp_t()
X1 = np.fft.fft(y1)
X2 = np.fft.fft(y2)
X1[0]=0
X2[0]=0
freqs = np.fft.fftfreq(len(t), t[1] - t[0])
idx0 = np.argmax(np.abs(X1))
phase_x1 = np.angle(X1[idx0])
f1=freqs[idx0]
idx = np.argmax(np.abs(X2))
f22=freqs[idx]
print(f22)
phase_x2 = np.angle(X2[idx0])
f2=freqs[idx0]
phase_difference = phase_x2 - phase_x1
phase_difference = (phase_difference + np.pi) % (2 * np.pi) - np.pi
x=t
if __name__=="__main__":
    print("相位差:", phase_difference)
    print("x2的主频率似乎不是10Hz",f22)
    fig, ax1 = plt.subplots()
    ax1.plot(x, y1, 'b-', label='move of x')
    ax1.plot(x,0.4*np.sin(2*np.pi*f1*x+phase_x1+np.pi/2)+0.5,'r--',label='fitting pic')
    ax1.set_xlabel('t/s')
    ax1.set_ylabel(r'x_move/$\mu$m')
    ax1.tick_params(axis='y')
    ax2 = ax1.twinx()
    ax2.plot(x, y2, 'g-', label='value of QPD')
    ax2.plot(x,600*np.sin(2*np.pi*f2*x+phase_x2+np.pi/2)-2755,'r--')
    ax2.set_ylabel('QPD')
    ax2.tick_params(axis='y')
    fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
    plt.show()












    # plt.plot(t,y1,'b',label='original pic')
    # plt.plot(t,y2,'b')
    # plt.plot(x,np.sin(2*np.pi*f1*x+phase_x1),'r--',label='fitting pic')
    # plt.plot(x,np.sin(2*np.pi*f2*x+phase_x2),'r--')
    # plt.legend(loc='upper right')
    # plt.show()












"""
熙神太巨辣！！！
对的√
"""