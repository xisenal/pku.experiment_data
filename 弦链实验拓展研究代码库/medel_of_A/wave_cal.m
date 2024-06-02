clear;
a1=680e-9;
a2=1290e-9;
b1=815e-9;
b2=685e-9;
n1=2.82;
n2=1.46;
lambda=1540e-9;
k=2*pi/lambda;
xs=[a1 a1+b1 2*a1+b1 2*(a1+b1) 3*a1+2*b1 3*(a1+b1) 4*a1+3*b1 4*(a1+b1)+a2 4*(a1+b1)+a2+b2 4*(a1+b1)+2*a2+b2 4*(a1+b1)+2*(a2+b2) 4*(a1+b1)+3*a2+2*b2 4*(a1+b1)+3*(a2+b2) 4*(a1+b1)+4*a2+3*b2 4*(a1+b1+a2+b2) ];
ns=[n1 n2 n1 n2 n1 n2 n1 n2 n1 n2 n1 n2 n1 n2 n1];
M1=[-1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0];
M2=[1 n1 -n1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0];
Mtrash=[M1;M2];

for j=1:14
    Mj=[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0];
    Mj(2*j)=exp(1j*ns(j)*xs(j)*k);
    Mj(2*j+1)=exp(-1j*ns(j)*k*xs(j));
    Mj(2*j+2)=-exp(1j*ns(j+1)*k*xs(j));
    Mj(2*j+3)=-exp(-1j*ns(j+1)*k*xs(j));
    Mtrash=[Mtrash;Mj];
    Mj=[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0];
    Mj(2*j)=ns(j)*exp(1j*ns(j)*xs(j)*k);
    Mj(2*j+1)=-ns(j)*exp(-1j*ns(j)*k*xs(j));
    Mj(2*j+2)=-ns(j+1)*exp(1j*ns(j+1)*k*xs(j));
    Mj(2*j+3)=ns(j+1)*exp(-1j*ns(j+1)*k*xs(j));
    Mtrash=[Mtrash;Mj];
end

M3=[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 exp(1j*ns(15)*k*xs(15)) exp(-1j*ns(15)*k*xs(15)) -exp(1j*1*k*xs(15))];
M4=[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 exp(1j*ns(15)*k*xs(15))*ns(15) -exp(-1j*ns(15)*k*xs(15))*ns(15) -exp(1j*1*k*xs(15))*1];
Mtrash=[Mtrash;M3;M4];
Mans=[1;1;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0];
ansx=linsolve(Mtrash,Mans);
xss=[0 a1 a1+b1 2*a1+b1 2*(a1+b1) 3*a1+2*b1 3*(a1+b1) 4*a1+3*b1 4*(a1+b1)+a2 4*(a1+b1)+a2+b2 4*(a1+b1)+2*a2+b2 4*(a1+b1)+2*(a2+b2) 4*(a1+b1)+3*a2+2*b2 4*(a1+b1)+3*(a2+b2) 4*(a1+b1)+4*a2+3*b2 4*(a1+b1+a2+b2) ];
figure(1)
for i=1:15
   A=ansx(i*2);
   B=ansx(i*2+1);
   xls=linspace(xss(i),xss(i+1),1000);
   E=A*exp(1j*ns(i)*k*xls)+B*exp(-1j*ns(i)*k*xls);
   Ereal=real(E);
   h=plot(xls*1e9,abs(Ereal),Color="red",LineWidth=2,DisplayName='E component');
   hold on;
end
for x=xss
    H=xline(x*1e9,'b--',LineWidth=1,DisplayName="Crystal boundary");
    hold on;
end
xlabel('coordinate/nm')
ylabel('The relative strength of electric field')
legend([H,h])

