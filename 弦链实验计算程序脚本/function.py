import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange

#前置函数：
def T_mesh(p):
   A=np.array([[np.cos(p),np.sin(p)],[-np.sin(p),np.cos(p)]])
   return A

#函数一：执行运算本征频率：
def cal_freq(tau,m_b,mu_0,a_num,F_T,N):
    ita=m_b/(mu_0*a_num)
    delta = np.linspace(0, 10, 100000)
    nope = []
    ans = []
    for i in trange(100000):
        delta_num = delta[i]
        phi = np.array([0, 1])
        phi = phi.T
        M = np.array([[1, 0], [-ita * delta_num, 1]])
        phi = T_mesh(delta_num * (1 - tau)) @ M @ T_mesh(delta_num * tau) @ phi
        for k in range(2,N+1):
            phi = T_mesh(delta_num * (k - tau - np.floor(k - tau))) @ M @ T_mesh(
            delta_num * (np.floor(k - tau) - k + tau + 1)) @ phi
        nope.append(abs(phi[0]))
    range_by = np.arange(1, 100000 - 1)
    for i in range_by:
        if nope[i - 1] > nope[i] and nope[i] < nope[i + 1]:
            ans.append(delta[i])
    pop = np.sqrt(F_T / (mu_0 * a_num ** 2)) / (2 * np.pi)
    for i in range(len(ans)):
        ans[i] = ans[i] * pop
    print(f'{N}个小球，边界为{tau}时的本征频率为：')
    print(ans)
    return ans



#函数二：绘制波函数：
def cal_y_fig(tau,m_b,mu_0,a_num,F_T,N):
    ita = m_b / (mu_0 * a_num)
    # 设置求解频率：
    Omega=input("请输入计算的频率/Hz")
    omega=eval(Omega)
    pop = np.sqrt(F_T / (mu_0 * a_num ** 2)) / (2 * np.pi)
    delta = omega / pop
    # 设置对应条件的M矩阵
    M = np.array([[1, 0], [-ita * delta, 1]])
    # 设置求解长度范围
    x = np.linspace(-tau, N - tau, 100000)
    y = [0]

    # 求解x位置上的y值
    def solve_y(w):
        phi = np.array([0, 1])
        phi = phi.T
        if w < 0:
            phix = T_mesh(delta * (w + tau)) @ phi
            return phix
        elif 0 <= w < 1:
            phix = T_mesh(delta * w) @ M @ T_mesh(delta * tau) @ phi
            return phix
        else:
            phi_x = solve_y(w - 1)
            phiarr = np.array(phi_x)
            phiarr = phiarr.T
            phix = T_mesh(delta * (w - np.floor(w))) @ M @ T_mesh(delta * (np.floor(w) - w + 1)) @ phiarr
            return phix

    arri = np.arange(1, 100000)
    for i in arri:
        phi_arr = solve_y(x[i])
        y.append(phi_arr[0])

    for i in arri:
        if y[i - 1] * y[i] < 0:
            print(x[i])

    y1 = [-a for a in y]
    xp = x[:]
    yp = y[:]
    y1p = y1[:]
    plt.plot(xp, yp)
    plt.plot(xp, y1p)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'wave of N={N},t={tau},f={omega}Hz')
    plt.show()



#函数三：输出频带底或顶的频率值，并绘制Dirac梳模型的函数图：
def cal_Dirac(mu_0,m_b,a_num,F_T):
    fx = np.linspace(0, 1000, 100000)
    fx = np.array(fx)
    f1 = np.cos(np.sqrt(mu_0 / F_T) * 2 * np.pi * a_num * fx) - ((m_b * 2 * np.pi * fx) / (2 * F_T)) * np.sqrt(
        F_T / mu_0) * np.sin(np.sqrt(mu_0 / F_T) * 2 * np.pi * a_num * fx)
    f2 = np.ones(100000)
    f2 = np.array(f2)
    f3 = abs(f1) - f2
    for i in range(100, 100000):
        if f3[i - 1] * f3[i] < 0:
            print(fx[i])
    plt.plot(fx, f1)
    plt.show()




#函数四：计算N个小球，某个带隙态中的本征频率随tau的变化曲线：
def cal_bsss(m_b,mu_0,a_num,F_T,N):
    a=eval(input("你想计算的是第几带隙态捏？（虽然我这么问，但是你输入的只能是1或者2）"))
    ita = m_b / (mu_0 * a_num)
    tmd = np.linspace(0, 1, 100)
    fignum = []
    for j in trange(100):
        tau = tmd[j]
        # 设置求解区间：
        delta = np.linspace(0, 7, 10000)
        nope = []
        ans = []
        for i in range(10000):
            delta_num = delta[i]
            phi = np.array([0, 1])
            phi = phi.T
            M = np.array([[1, 0], [-ita * delta_num, 1]])
            phi = T_mesh(delta_num * (1 - tau)) @ M @ T_mesh(delta_num * tau) @ phi
            for k in range(2,N+1):
                phi = T_mesh(delta_num * (k - tau - np.floor(k - tau))) @ M @ T_mesh(
                delta_num * (np.floor(k - tau) - k + tau + 1)) @ phi
            nope.append(abs(phi[0]))
        range_by = np.arange(1, 10000 - 1)
        for i in range_by:
            if nope[i - 1] > nope[i] and nope[i] < nope[i + 1]:
                ans.append(delta[i])
        pop = np.sqrt(F_T / (mu_0 * a_num ** 2)) / (2 * np.pi)
        for i in range(len(ans)):
            ans[i] = ans[i] * pop
        if N==6:
            if a==1:
                fignum.append(ans[5])
            elif a==2:
                fignum.append(ans[11])
            else:
                print("哎呦你干嘛")
        elif N==7:
            if a==1:
                fignum.append(ans[6])
            elif a==2:
                fignum.append(ans[13])
            else:
                print("哎呦你干嘛")
        else:
            print("抱歉这个程序不支持N！=6或7的计算")
    list_name_fig=['first','second']
    plt.plot(tmd, fignum)
    plt.xlabel('tau')
    plt.ylabel(f'Intrinsic frequency in the {list_name_fig[a-1]} band edge state/Hz')
    plt.show()
    # 5,11
    # 6,13
