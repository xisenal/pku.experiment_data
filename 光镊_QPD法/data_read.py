import numpy as np
def read_single():
    x=[]
    y=[]
    with open('single.txt','r',encoding='utf-8') as file:
        for line in file:
            if line[0]=='[' or line[0]=='#':
                continue
            else:
                num=line.split()
                xnum=eval(num[0])
                ynum=eval(num[1])
                x.append(xnum)
                y.append(ynum)
    return x,y


def read_tri():
    x=[]
    y=[]
    with open('tri.txt','r',encoding='utf-8') as file:
        for line in file:
            if line[0]=='[' or line[0]=='#':
                continue
            else:
                num=line.split()
                xnum=eval(num[0])
                ynum=eval(num[1])
                x.append(xnum)
                y.append(ynum)
    return x,y

def imp_t():
    start = 0
    step = 5e-5
    num_elements = 30000
    sequence = np.arange(start, start + step * num_elements, step)
    return sequence