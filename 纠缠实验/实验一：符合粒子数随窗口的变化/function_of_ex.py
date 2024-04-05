import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import poisson
from scipy.optimize import minimize

names_index=["1ns.txt","1.5ns.txt","2ns.txt","2.5ns.txt","3ns.txt","3.5ns.txt","4ns.txt","4.5ns.txt","7.5ns.txt","10ns.txt","15ns.txt"]
times_index=[1,1.5,2,2.5,3,3.5,4,4.5,7.5,10,15]

#这里给出两种拟合方式，极大似然估计法和舍选法扩大样本空间：
def poisson_mle(data):
    def neg_log_likelihood(lambda_, data):
        return -np.sum(-lambda_ + np.array(data) * math.log(lambda_) - np.sum(np.array([math.log(math.factorial(x)) for x in data])))
    initial_guess = np.mean(data)
    result = minimize(neg_log_likelihood, initial_guess, args=(data,), method='L-BFGS-B')
    lambda_mle = result.x[0]
    return lambda_mle
def expand_data(data, num_samples):
    expanded_data = []
    max_data = max(data)
    while len(expanded_data) < num_samples:
        new_data = np.random.poisson(np.mean(data), num_samples)
        keep_indices = np.where(new_data <= max_data)[0]
        expanded_data.extend(new_data[keep_indices])
    return expanded_data

def get_mean_name(name):
    a=[]
    with open(name,'r',encoding='utf-8') as file:
        for line in file:
            try:
                number = int(line.strip()) 
                a.append(number)
            except ValueError:
                print(f"无法将行 '{line.strip()}' 解析为整数。")
    mean_a=np.mean(a)
    return mean_a

def get_list(name):
    a=[]
    with open('15ns.txt','r',encoding='utf-8') as file:
        for line in file:
            try:
                number = int(line.strip()) 
                a.append(number)
            except ValueError:
                print(f"无法将行 '{line.strip()}' 解析为整数。")
    return a

def get_start_hist(a,bin_numbers):
    a=plt.hist(a,bins=bin_numbers,color='blue',alpha=0.7)
    plt.show()
    return a

def get_mean(a):
    return np.mean(a)

def get_sigma(a):
    mean_a=np.mean(a)
    arr=np.array(a)
    arr=arr**2
    mean_a2=np.mean(arr)
    sigma=mean_a2-mean_a**2
    return sigma










def draw_mean():
    mean_list=[]
    for name in names_index:
        mean_list.append(get_mean_name(name))
    plt.plot(times_index,mean_list,marker='*', markersize=6, color='b')
    plt.xlabel('t/ns')
    plt.ylabel('arg(N)')
    plt.title('N-t')
    plt.show()
def test1():
    a=get_list("15ns.txt")
    sigma=get_sigma(a)
    mean_a=get_mean(a)
    print("原始数据给出的均值和方差：",mean_a,sigma)
    get_start_hist(a,10)
def test2():
    a=get_list('10ns.txt')
    a_=expand_data(a,100000)
    print("expand arg =",np.mean(a_))
    get_start_hist(a_,100)

test2()
draw_mean()


