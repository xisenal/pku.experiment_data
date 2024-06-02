%设置晶体参数
N=4;
l1=680e-9;
L1=685e-9;
l2=815e-9;
L2=1290e-9;
e1=2.82^2;
e2=1.46^2;
epsilon_0=8.854e-12;
mu_0=4*pi*1e-7;
%设置频谱范围
fre=linspace(1e14,2.5e14,100000);
c=3e8;
%%求出单周期特征矩阵，正入射假设下
n1=sqrt(e1);
n2=sqrt(e2);
lbd=c./fre;
lbd=flip(lbd);
T_f=zeros(size(lbd));
i=1;
for lamd=lbd
    beta1=(2*pi/lamd)*n1*l1;
    beta2=(2*pi/lamd)*n2*l2;
    beta11=(2*pi/lamd)*n2*L1;
    beta22=(2*pi/lamd)*n1*L1;
    p1=sqrt(epsilon_0/mu_0)*n1;
    p2=sqrt(epsilon_0/mu_0)*n2;
    p0=sqrt(epsilon_0/mu_0);
    M_of1=[cos(beta1),-1j*sin(beta1)/p1;-1j*p1*sin(beta1),cos(beta1)];
    M_of2=[cos(beta2),-1j*sin(beta2)/p2;-1j*p2*sin(beta2),cos(beta2)];
    M_of11=[cos(beta11),-1j*sin(beta11)/p2;-1j*p2*sin(beta11),cos(beta11)];
    M_of22=[cos(beta22),-1j*sin(beta22)/p1;-1j*p1*sin(beta22),cos(beta22)];
    M_of_period=M_of1*M_of2;
    M_of_period1=M_of11*M_of22;
    % M_form=M_of_period^N;
    % 初始化M_form为单位矩阵
    M_form = eye(2);
    % 使用循环逐步相乘，以提高数值稳定性
    for k = 1:N
        M_form = M_form * M_of_period;
    end
    M_form1 = eye(2);
    % 使用循环逐步相乘，以提高数值稳定性
    for k = 1:N
        M_form1 = M_form1 * M_of_period1;
    end
    M_form=M_form*M_form1;
    Trans=(2*p0)/((M_form(1,1)+M_form(1,2)*p1)*p0+(M_form(2,1)+M_form(2,2)*p1));
    Trans=abs(Trans)^2;
    T_f(i)=Trans;
    i=i+1;
end
figure(1)
plot(lbd,T_f)