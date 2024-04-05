import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_excel('数据整理.xlsx', sheet_name='组合')
N=df.iloc[2:6, 6].tolist()
t_N=df.iloc[2:6,7].tolist()
plt.plot(N,t_N,marker='*',markersize=6,color='blue')
plt.show()