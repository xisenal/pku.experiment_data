import numpy as np
from numpy.fft import fft
import matplotlib.pyplot as plt
pi = np.pi
def fft_calc(x, f_s, x_size, nfft):
    w = np.hanning(nfft)                            # 加汉尼窗
    cnt = x_size // nfft                            # 计算数据长度可以覆盖几个窗口
    # 将输入数据长度补齐为窗口长度的整数倍，补齐数据为0
    # 此方式可以避免输入数据长度小于窗口长度
    if cnt == 0:                                    # 用0在数据尾部补齐
        x_pad = np.pad(x, (0, int(nfft - x_size)))
    else:
        x_pad = np.pad(x, (0, int(x_size - cnt * nfft)))
    cnt = len(x_pad) // nfft                            # 更新补齐的数据长度可以覆盖几个窗口
    # 以窗口长度计算输入数据的FFT
    tmp = []
    for i in range(cnt):                            # 窗与窗之间数据不重叠
        p = fft(w * x_pad[i * nfft:(i+1) * nfft])       # 计算加窗的FFT并乘以调整系数
        tmp.append(p)                               # 每个窗的结果
    # 将所有计算取平均值
    fft_result = np.mean(tmp, axis=0)               # 将所有窗平均得到最终结果
    # 根据采样宽度计算幅值
    amp = abs(fft_result)*2 / (nfft / 2)
    # 对直流分量额外调整
    amp[0] /= 2
    # 根据FFT特性，取一半频谱即可
    amp_half = amp[:int(len(amp) / 2)+1]
    # 根据采样频率和采样点数，计算频率分辨率，并得到对应的频率坐标
    freq = np.arange(int(len(amp) / 2)+1) * f_s/nfft
    return amp_half, freq

y1=[]
y2=[]
with open('wyxhg1.txt','r',encoding='utf-8') as file:
    for line in file:
        if line[0]=='D':
            continue
        else:
            y1.append(eval(line[21:28]))
            y2.append(eval(line[33:40]))

data=np.array(y1[5000:-2000])

x=np.array(data)
fs=5000
nfft=fs
N = len(data)

(amp, freq) = fft_calc(x, fs , N , nfft)

print(amp[415:420])
fig = plt.figure(figsize=(8, 6))
plt.plot(freq, amp, color="blue")

plt.title('FFT result')
plt.xlabel('Wave Lenth /100nm')
plt.ylabel('urad/Hz')

# plt.xscale('log')
ax = plt.gca()
plt.grid(which='both', axis='both')

plt.show()
print(amp[40:50])