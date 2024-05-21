from liquit_30 import pic_read_30
from liquit_40 import pic_read_40
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pic_read_30.execute_code=False
pic_read_40.execute_code=False

t1_30=pic_read_30.t1
t2_30=pic_read_30.t2
x1_30=pic_read_30.x1
x2_30=pic_read_30.x2

t1_40=pic_read_40.t1
t2_40=pic_read_40.t2
x1_40=pic_read_40.x1
x2_40=pic_read_40.x2

plt.rcParams['font.family'] = 'Microsoft YaHei'
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(t1_30,x1_30,label='参考物的运动')
plt.plot(t2_30,x2_30,label='光镊抓取物的运动')
plt.xlabel('t/s')
plt.ylabel(r'x/$\mu$m')
plt.title('A=30时的图像')
plt.legend(loc='upper right')
plt.subplot(1,2,2)
plt.plot(t1_40,x1_40,label='参考物的运动')
plt.plot(t2_40,x2_40,label='光镊抓取物的运动')
plt.xlabel('t/s')
plt.ylabel(r'x/$\mu$m')
plt.title('A=40时的图像')
plt.legend(loc='upper right')
plt.show()