import numpy as np
import matplotlib.pyplot as plt
#定义数据点
x=np.array([40,60,80,100])
y=np.array([0.2538,0.4012,0.5418,0.6212])
#计算斜率和截距
slope,intercept=np.polyfit(x,y,1)
#计算R^2值
r2=np.corrcoef(x,y)[0,1]**2
#绘制散点图和拟合线
plt.scatter(x,y)
plt.plot(x,slope*x+intercept)
plt.show()
#打印斜率、截距和R^2值
print("斜率:",slope)
print("截距:",intercept)
print("R^2值:",r2)
