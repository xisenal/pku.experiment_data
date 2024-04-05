#生成一个大概的N-t_N图：
import numpy as np
import matplotlib.pyplot as plt

N=[1.5,2.5,3.5,4.5,5.5,6.5]
t_N=[313,72,13,9,4,3]
plt.plot(N,t_N,marker='*',markersize=6,color='blue')
plt.show()