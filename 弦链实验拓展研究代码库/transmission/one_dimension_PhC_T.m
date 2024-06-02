%设置晶体参数
N=4;
l1=0.06;
l2=0.24;
e1=36;
e2=1;
epsilon_0=8.854e-12;
mu_0=4*pi*1e-7;
% epsilon_0=1;
% mu_0=1;
%设置频谱范围
fre=linspace(10,150,100000);
c=sqrt(8.93);
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
    p1=sqrt(epsilon_0/mu_0)*n1;
    p2=sqrt(epsilon_0/mu_0)*n2;
    p0=sqrt(epsilon_0/mu_0);
    M_of1=[cos(beta1),-1j*sin(beta1)/p1;-1j*p1*sin(beta1),cos(beta1)];
    M_of2=[cos(beta2),-1j*sin(beta2)/p2;-1j*p2*sin(beta2),cos(beta2)];
    M_of_period=M_of1*M_of2;
    % M_form=M_of_period^N;
    % 初始化M_form为单位矩阵
    M_form = eye(2);
    % 使用循环逐步相乘，以提高数值稳定性
    for k = 1:N
        M_form = M_form * M_of_period;
    end
    Trans=(2*p0)/((M_form(1,1)+M_form(1,2)*p1)*p0+(M_form(2,1)+M_form(2,2)*p1));
    Trans=abs(Trans)^2;
    T_f(i)=Trans;
    i=i+1;
end
figure(1)
plot(fre,T_f)

