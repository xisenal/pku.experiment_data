n1=3;
k=2*pi/1.3;
A=[-1 1 1 0;1 n1 n1 0;0 exp(1j*k*n1) exp(-1j*k*n1) -exp(1j*k);0 n1*exp(1j*k*n1) -n1*exp(-1j*k*n1) -exp(1j*k)];
b=[1;1;0;0];
x=linsolve(A,b);
figure(1)
xs=[-1,0,1,2];
A0=1;
B0=x(1);
xls=linspace(-1,0,1000);
E0=A0*exp(1j*k*xls)+B0*exp(-1j*k*xls);
E0=real(E0);
plot(xls,E0)
hold on;
A1=x(2);
B1=x(3);
xls=linspace(0,1,1000);
E1=A1*exp(1j*k*n1*xls)+B1*exp(-1j*n1*k*xls);
E1=real(E1);
plot(xls,E1)
hold on;
A2=x(4);
xls=linspace(1,2,1000);
E2=A2*exp(1j*k*xls);
E2=real(E2);
plot(xls,E2)