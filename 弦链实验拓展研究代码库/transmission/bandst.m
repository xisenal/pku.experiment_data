clc,clear  % TE
c=3*10^8; m0=4*pi*10^(-7); e0=8.854*10^(-10);
n(1)=2.82; n(2)=1.46;
d(1)=680;d(2)=815;  % 输入两层厚度比例即可，最后坐标是归一化的
D=d(1)+d(2);    % A/B排列
No=3;  % 输入计算禁带数范围
theta=[0 0 0];    % 垂直入射
eta=zeros; eta0=sqrt(e0/m0);
n0=(n(1)*d(1)+n(2)*d(2))/D;
k0=pi/D;
omega0=c*k0/n0;  % 1st 禁带中心频率
omegaunit=c/d(1);
omega=linspace(0,No*omega0,1000);
kd=zeros;

for i=1:length(omega)
delta=zeros; eta=zeros;
    for j=1:2
        delta(j)=omega(i)*n(j)*d(j)*cos(theta(j))/c;
        eta(j)=sqrt(e0/m0)*n(j)*cos(theta(j));
    end
    temp=acos(cos(delta(1))*cos(delta(2))-(eta(1)/eta(2)+eta(2)/eta(1))*sin(delta(1))*sin(delta(2))/2);
    if imag(temp)~=0
        continue
    end
    kd(i)=temp;
end

figure
plot(kd,omega(1:length(kd))/omegaunit,'LineWidth',2,Color="red");
xlabel('k_zL');ylabel('{\omega}a/c')
title('The Band Structure of PhC')
xlim([0 pi])