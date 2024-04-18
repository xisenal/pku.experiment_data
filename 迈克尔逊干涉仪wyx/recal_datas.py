import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1=pd.read_excel('wyxhg.xlsx', sheet_name='Sheet1')
t=df1.iloc[1:4611, 0].tolist()
y1=df1.iloc[1:4611,1].tolist()
y1=[int(item[:-1]) for item in y1]
y2=df1.iloc[1:4611,3].tolist()
y2=[int(item[:-1]) for item in y2]
plt.figure(figsize=(15, 5))
plt.subplot(1,3,1)
plt.plot(t,y1)
plt.subplot(1,3,2)
plt.plot(t,y2)
plt.subplot(1,3,3)
plt.plot(t,y1,color='red',label='ch1')
plt.plot(t,y2,color='blue',label='ch2')
plt.legend()
plt.show()