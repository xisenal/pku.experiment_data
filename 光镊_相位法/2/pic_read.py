import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_excel(r'C:\Users\20761\Desktop\光镊\相位法\2\2.xlsx')
t1=data.iloc[2:58,0].tolist()
x1=data.iloc[2:58,1].tolist()
t2=data.iloc[2:58,3].tolist()
x2=data.iloc[2:58,4].tolist()
def arr(x):
    return np.array(x)
t1=arr(t1)
t2=arr(t2)
x1=arr(x1)
x2=arr(x2)
x2*=10
x2-=3500
plt.plot(t1,x1)
plt.plot(t2,x2)
plt.show()