import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df1=pd.read_excel('实验数据.xlsx', sheet_name='theta1=0')
theta2=df1.iloc[1:19, 0].tolist()
N1=df1.iloc[1:19,26].tolist()
df2=pd.read_excel('实验数据.xlsx', sheet_name='theta1=45')
N2=df2.iloc[1:19,26].tolist()
df3=pd.read_excel('实验数据.xlsx', sheet_name='theta1=90')
N3=df3.iloc[1:19,26].tolist()
df4=pd.read_excel('实验数据.xlsx', sheet_name='theta1=135')
N4=df4.iloc[1:19,26].tolist()
plt.plot(theta2,N1,marker='*',markersize=6,color='blue',label='theta1=0')
plt.plot(theta2,N2,marker='*',markersize=6,color='red',label='theta1=45')
plt.plot(theta2,N3,marker='*',markersize=6,color='orange',label='theta1=90')
plt.plot(theta2,N4,marker='*',markersize=6,color='pink',label='theta1=135')
plt.legend()
plt.show()