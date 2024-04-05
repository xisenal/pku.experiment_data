import numpy as np
import  matplotlib.pyplot as plt
from tqdm import trange
import function as fp
import re
data=[]
with open('data_of_ex.txt','r', encoding='utf-8') as file:
    for line in file:
        if line[0]=='#':
            continue
        else:
            meanit=line
            pattern = r'[-+]?\b\d*\.\d+|\b\d+|\d+e[-+]?\d+\b'
            matches = re.findall(pattern, meanit)
            if matches:
                for match in matches:
                    data.append(eval(match))
m_b=data[0]
mu_0=data[1]
F_T=data[2]
a_num=data[3]
N=data[4]
tau=data[5]
bfuc=[]
with open('function_user.txt','r',encoding='utf-8') as file:
    for line in file:
        if line[0]=='#':
            continue
        else:
            if line[0]=='T' or line[0]=='t':
                bfuc.append(True)
            elif line[0]=='F' or line[0]=='f':
                bfuc.append(False)
            else:
                print("格式错误！！！！")

if bfuc[0]:
    fp.cal_freq(tau,m_b,mu_0,a_num,F_T,N)
if bfuc[1]:
    fp.cal_y_fig(tau,m_b,mu_0,a_num,F_T,N)
if bfuc[2]:
    fp.cal_Dirac(mu_0,m_b,a_num,F_T)
if bfuc[3]:
    fp.cal_bsss(m_b,mu_0,a_num,F_T,N)
