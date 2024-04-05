%创建两个计算用的坐标矩阵
N=128;
L=60;
dx=L/N;   
dy=L/N;
x=dx*(-N/2:N/2-1);
y=dy*(-N/2:N/2-1)';
kx=(-N/2:N/2-1).*2*pi/L;   
ky=(-N/2:N/2-1)'.*2*pi/L; 

%转换成矩阵的形式进行计算
[X,Y]=meshgrid(x,y);
[KX,KY]=meshgrid(kx,ky);

%重新设置方程的参数(单位制采用微米/ps/meV)
h_bar=0.658;
gamma_c=0.08;
gamma_r=0.12;
R=0.01;
g_c=0.003;
g_r=0.006;
w_g=50;
P_0=1.1;

%设置一部分国际单位制：
hbar=1.05457*10^(-34);
m_e=9.10938*10^(-31);
m_eff=10^(-4)*m_e;

%构建一个势能函数（双环）
V0=0.45;  
Omega_R=8;
Omega_r=5;
d=5;
N_index = 10^3;
V = -V0 * exp(-((X.^2+Y.^2)/(Omega_R)^2).^N_index).*(1-exp(-((X.^2+Y.^2)/(Omega_r)^2).^N_index)) - V0 * exp(-((X.^2+Y.^2)/(2*Omega_R+d-Omega_r)^2).^N_index).*(1-exp(-((X.^2+Y.^2)/(d+Omega_R)^2).^N_index));

figure(1)
pcolor(x,y,V)
shading interp; 
colorbar; 
xlabel('x(μm)');ylabel('y(μm)')
title('V(meV)')

%设置迭代的时间参量：
dt=0.1;
tfinal = 5500;   
Round = round(tfinal/dt);

%明确几个函数关系：
Pmesh=P_0*exp(-(X.^2+Y.^2)/(w_g)^2);
numfft=exp(-(1j*hbar/(2*m_eff))*dt*(KX.^2+KY.^2));
I = ones(N,N);


%设置初始状态：
psi = (1/L)*ones(N,N).*exp(1i*angle(X+1i*Y));
n = 0*ones(N,N);

%执行RK4方法进行迭代运算：
for k=1:Round
    k1p=(1/(1j*h_bar))*((-1i*h_bar*gamma_c/2)*I+g_c*abs(psi).^2+(g_r+1i*h_bar*R/2)*n + V).*psi;
    k1n=(-gamma_r*I-R*abs(psi).^2).*n + Pmesh;

    k2p=(1/(1j*h_bar))*((-1i*h_bar*gamma_c/2)*I+g_c*abs(psi+k1p*dt/2).^2+(g_r+1i*h_bar*R/2)*(n+k1n*dt/2) + V).*(psi+k1p*dt/2);
    k2n=(-gamma_r*I-R*abs(psi+k1p*dt/2).^2).*(n+k1n*dt/2) + Pmesh;

    k3p=(1/(1j*h_bar))*((-1i*h_bar*gamma_c/2)*I+g_c*abs(psi+k2p*dt/2).^2+(g_r+1i*h_bar*R/2)*(n+k2n*dt/2) + V).*(psi+k2p*dt/2);
    k3n=(-gamma_r*I-R*abs(psi+k2p*dt/2).^2).*(n+k2n*dt/2) + Pmesh;
    
    k4p=(1/(1j*h_bar))*((-1i*h_bar*gamma_c/2)*I+g_c*abs(psi+k3p*dt).^2+(g_r+1i*h_bar*R/2)*(n+k3n*dt) + V).*(psi+k3p*dt);
    k4n=(-gamma_r*I-R*abs(psi+k3p*dt).^2).*(n+k3n*dt) + Pmesh;

    psi=psi+dt*(k1p+2*k2p+2*k3p+k4p)/6;
    n=n+dt*(k1n+2*k2n+2*k3n+k4n)/6;

    psi=fft2(psi);
    psi=fftshift(psi);
    psi=psi.*numfft;
    psi=fftshift(psi);
    psi=ifft2(psi);
end


figure(2)
surf(x,y,abs(psi).^2)
xlabel('x(μm)');ylabel('y(μm)')
title('|Ψ|^2（μm^-^2）')

figure(3)
pcolor(x,y,abs(psi).^2)
shading interp; 
colorbar; 
colormap(jet);
xlabel('x(μm)');ylabel('y(μm)');
title('|Ψ|^2（μm^-^2）')

figure(4)
pcolor(x,y,angle(psi))
shading interp; 
colorbar; 
colormap(jet);
xlabel('x(μm)');ylabel('y(μm)');
title('angle(Ψ)')

figure(5)
pcolor(x,y,n)
shading interp; 
colorbar; 
colormap(jet);
xlabel('x(μm)');ylabel('y(μm)');
title('n(μm^-^2)')