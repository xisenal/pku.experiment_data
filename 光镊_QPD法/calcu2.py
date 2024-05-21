import csv
import numpy as np
from matplotlib import pyplot as plt
from numpy.fft import fft

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

lis=[]
with open('data1.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        row=row['123']
        data=row.split(";")
        lis.append(int(data[-1]))
  
liss=[]
for i in lis:
    liss.append(i)

sum=0
for i in liss:
    sum+=i
ave=sum/len(liss)
lis=[]
for i in liss:
    lis.append(i-ave)
        

    
x=[i for i in range(len(lis))]
x=np.array(x)
y=np.array(lis)

fs=5000
nfft=fs
N = len(y)
(amp, freq) = fft_calc(y, fs , N , nfft)
freq=freq[0:500]
amp=amp[0:500]

if __name__=="__main__":
    plt.plot(freq, amp, color="blue")
    plt.show()

    dif=0
    for i in lis:
        dif+=i*i
    dif/=len(lis)



    k=103
    dif=dif/k/k
    print(dif)