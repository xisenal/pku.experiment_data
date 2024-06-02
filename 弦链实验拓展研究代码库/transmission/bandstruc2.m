clc,clear
mode=0;  %1 for TE; 0 for TM
No=4;  % 输入计算禁带数范围
Nm=2*No;  % band edge 条数
c=3*10^8; m0=4*pi*10^(-7); e0=8.854*10^(-10);
n(1)=2.82; n(2)=1.46;
d(1)=680e-9;d(2)=815e-9;  
L=d(1)+d(2);    % 两介质
%theta=[0 0 0];    % 垂直入射
n0=(n(1)*d(1)+n(2)*d(2))/L;
k0=pi/L;
omega0=c*k0/n0;  % 禁带中心基频
omegaunit=c/L;
kunit=2*pi/L;
Nky=200;
Nomega=No*2500;
omega=linspace(0,No*omega0,Nomega);
N=10;  % 周期数
k=zeros;  % k:=kz
ky=linspace(0,2,Nky)*kunit;

% projected band edge
e=5e-1*kunit;
edge=ones(length(ky),Nm)*omega(end);

for i=1:length(ky)
    m=1;
for j=1:length(omega)
        %omega2(i,j)=omega(j);
        %ky2(i,j)=ky(i);
        for q=1:length(n)
        kz(q)=((n(q)*omega(j)/c)^2-ky(i)^2)^0.5; % 介质中kz
        end
    A=exp(1j*kz(1)*d(1))*(cos(kz(2)*d(2))+0.5j*sin(kz(2)*d(2))*(kz(2)/kz(1)+kz(1)/kz(2)))*mode...
     +exp(1j*kz(1)*d(1))*(cos(kz(2)*d(2))+0.5j*sin(kz(2)*d(2))*(n(1)^2/n(2)^2*kz(2)/kz(1)+n(2)^2/n(1)^2*kz(1)/kz(2)))*(1-mode);
    D=exp(-1j*kz(1)*d(1))*(cos(kz(2)*d(2))-0.5j*sin(kz(2)*d(2))*(kz(2)/kz(1)+kz(1)/kz(2)))*mode...
     +exp(-1j*kz(1)*d(1))*(cos(kz(2)*d(2))-0.5j*sin(kz(2)*d(2))*(n(1)^2/n(2)^2*kz(2)/kz(1)+n(2)^2/n(1)^2*kz(1)/kz(2)))*(1-mode);
    k(i,j)=1/L*acos(0.5*(A+D)); k(1,1)=0;  % 第一个总是发散
    if (mod(m,4)==1&&abs(imag(k(i,j)))==0)
        edge(i,m)=omega(j);
        m=m+1;     
        continue
    end    
    if mod(m,4)==2&&abs(real(k(i,j))-0.5*kunit)<e&&abs(imag(k(i,j)))>0
        edge(i,m)=omega(j);
        m=m+1;
        continue
    end    
    if mod(m,4)==3&&abs(real(k(i,j))-0.5*kunit)<e&&abs(imag(k(i,j)))==0
        edge(i,m)=omega(j);
        m=m+1;
        continue
    end 
    if mod(m,4)==0&&abs(real(k(i,j)))<e&&abs(imag(k(i,j-1)))>0
        edge(i,m)=omega(j);
        m=m+1;
        continue
    end     
end
    if m>Nm
        continue
    end
end

    ky_unit=ky./kunit;  % 行向量
    freq=edge./(2*pi)*1e-12;  % THz
figure
for m=1:Nm
    plot(ky_unit,freq(:,m))
    hold on
end
axis([ky_unit(1) ky_unit(end) freq(1,1) freq(end,end)-10])
xlabel('k_xL/2\pi');ylabel('f/THz')

% 填充能带阴影
P=400e-9;  % 横向周期(XY平面可以有周期结构)
ky_unit=ky*P/2/pi; % 转换为横向周期的 归一化布洛赫波矢
figure
for m=1:2:(Nm-1)

    fill([ky_unit,fliplr(ky_unit)],[freq(:,m)',fliplr(freq(:,m+1)')],[0.75 0.75 0.75])
    hold on
end
if mode==0
    title('TM wave band relationship')
else
    title('TE wave band relationship')
end

axis([ky_unit(1) ky_unit(end) freq(1,1) freq(end,end)-10])
xlabel('k_xL/2\pi');ylabel('f/THz')