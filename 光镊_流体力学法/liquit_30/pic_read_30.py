import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_excel(r'C:\Users\20761\Desktop\光镊\6\liquit_30\30.xlsx')

def anlis(x):
    a=[]
    b=[]
    for i,num in enumerate(x):
        if num>1:
            a.append(num)
        elif num<=0:
            b.append(num)
    num1,num2=np.mean(a),np.mean(b)
    return num1,num2,num1-num2

t1=data.iloc[2:288,0].tolist()
x1=data.iloc[2:288,1].tolist()
t2=data.iloc[2:288,3].tolist()
x2=data.iloc[2:288,4].tolist()
def arr(x):
    return np.array(x)
t1=arr(t1)
t2=arr(t2)
x1=arr(x1)
x2=arr(x2)
x1=(x1/628)*30-2.745
x2=(x2/628)*30-43
execute_code = True
if execute_code:
    print(anlis(x2))
    plt.plot(t1,x1)
    plt.plot(t2,x2)
    plt.show()


