clear;
lamd=1540e-9;
k=2*pi/lamd;
n1=2.82;
n2=1.46;
epsilon_0 = 8.854e-12;
mu_0 = 4*pi*1e-7; 
% n1=2.82;
% n2=1.46;
l1=680e-9;
l2=815e-9;
l3=685e-9;
l4=1290e-9;
M1=transcal(n1,l1);
M2=transcal(n2,l2);
M3=transcal(n2,l2+l4);
M4=transcal(n1,l3);
M5=transcal(n2,l4);
arr=[1;sqrt(epsilon_0/mu_0)];
arr1=M1*arr;
arr2=M2*arr1;
arr3=M1*arr2;
arr4=M2*arr3;
arr5=M1*arr4;
arr6=M2*arr5;
arr7=M1*arr6;
arr8=M3*arr7;
arr9=M4*arr8;
arr10=M5*arr9;
arr11=M4*arr10;
arr12=M5*arr11;
arr13=M4*arr12;
arr14=M5*arr13;
arr15=M4*arr14;
x=linspace(0,4*(l1+l2+l3+l4),100000);
Ess=x;
for i=1:length(Ess)
    if (Ess(i)>=0)&&(Ess(i)<=l1)
        Ess(i)=arr(1)*exp(-1j*n1*k*x(i));
    elseif (Ess(i)>l1)&&(Ess(i)<=l1+l2)
        Ess(i)=arr1(1)*exp(-1j*n2*k*x(i));
    elseif (Ess(i)>l1+l2)&&(Ess(i)<=2*l1+l2)
        Ess(i)=arr2(1)*exp(-1j*n1*k*x(i));
    elseif (Ess(i)>2*l1+l2)&&(Ess(i)<=2*(l1+l2))
        Ess(i)=arr3(1)*exp(-1j*n2*k*x(i));
    elseif (Ess(i)>2*(l1+l2))&&(Ess(i)<=3*l1+2*l2)
        Ess(i)=arr4(1)*exp(-1j*n1*k*x(i));
    elseif (Ess(i)>3*l1+2*l2)&&(Ess(i)<=3*(l1+l2))
        Ess(i)=arr5(1)*exp(-1j*n2*k*x(i));
    elseif (Ess(i)>3*(l1+l2))&&(Ess(i)<=4*l1+3*l2)
        Ess(i)=arr6(1)*exp(-1j*n1*k*x(i));
    elseif (Ess(i)>4*l1+3*l2)&&(Ess(i)<=4*(l1+l2)+l4)
        Ess(i)=arr7(1)*exp(-1j*n2*k*x(i));
    elseif (Ess(i)>4*(l1+l2)+l4)&&(Ess(i)<=4*(l1+l2)+l4+l3)
        Ess(i)=arr8(1)*exp(-1j*n1*k*x(i));
    elseif (Ess(i)>4*(l1+l2)+l4+l3)&&(Ess(i)<=4*(l1+l2)+2*l4+l3)
        Ess(i)=arr9(1)*exp(-1j*n2*k*x(i));
    elseif (Ess(i)>4*(l1+l2)+2*l4+l3)&&(Ess(i)<=4*(l1+l2)+2*l4+2*l3)
        Ess(i)=arr10(1)*exp(-1j*n1*k*x(i));
    elseif (Ess(i)>4*(l1+l2)+2*l4+2*l3)&&(Ess(i)<=4*(l1+l2)+3*l4+2*l3)
        Ess(i)=arr11(1)*exp(-1j*n2*k*x(i));
    elseif (Ess(i)>4*(l1+l2)+3*l4+2*l3)&&(Ess(i)<=4*(l1+l2)+3*l4+3*l3)
        Ess(i)=arr12(1)*exp(-1j*n1*k*x(i));
    elseif (Ess(i)>4*(l1+l2)+3*l4+3*l3)&&(Ess(i)<=4*(l1+l2)+4*l4+3*l3)
        Ess(i)=arr13(1)*exp(-1j*n2*k*x(i));
    elseif (Ess(i)>4*(l1+l2)+4*l4+3*l3)&&(Ess(i)<=4*(l1+l2)+4*l4+4*l3)
        Ess(i)=arr14(1)*exp(-1j*n1*k*x(i));
    end
end
Ewave=abs(real(Ess));


figure(1)
a1=680e-9;
a2=1290e-9;
b1=815e-9;
b2=685e-9;
xss=[0 a1 a1+b1 2*a1+b1 2*(a1+b1) 3*a1+2*b1 3*(a1+b1) 4*a1+3*b1 4*(a1+b1)+a2 4*(a1+b1)+a2+b2 4*(a1+b1)+2*a2+b2 4*(a1+b1)+2*(a2+b2) 4*(a1+b1)+3*a2+2*b2 4*(a1+b1)+3*(a2+b2) 4*(a1+b1)+4*a2+3*b2 4*(a1+b1+a2+b2) ];
for xee=xss
    xe=xee*1e9;
    xline(xe,'b--',LineWidth=1)
    hold on;
end

yyaxis left
h1=plot(x*1e9,Ewave,Color="red",LineWidth=2,DisplayName="E component");
ylabel('The relative strength of electric field')
hold on;




Ess=x;
for i=1:length(Ess)
    if (Ess(i)>=0)&&(Ess(i)<=l1)
        Ess(i)=arr(2)*exp(-1j*n1*k*x(i));
    elseif (Ess(i)>l1)&&(Ess(i)<=l1+l2)
        Ess(i)=arr1(2)*exp(-1j*n2*k*x(i));
    elseif (Ess(i)>l1+l2)&&(Ess(i)<=2*l1+l2)
        Ess(i)=arr2(2)*exp(-1j*n1*k*x(i));
    elseif (Ess(i)>2*l1+l2)&&(Ess(i)<=2*(l1+l2))
        Ess(i)=arr3(2)*exp(-1j*n2*k*x(i));
    elseif (Ess(i)>2*(l1+l2))&&(Ess(i)<=3*l1+2*l2)
        Ess(i)=arr4(2)*exp(-1j*n1*k*x(i));
    elseif (Ess(i)>3*l1+2*l2)&&(Ess(i)<=3*(l1+l2))
        Ess(i)=arr5(2)*exp(-1j*n2*k*x(i));
    elseif (Ess(i)>3*(l1+l2))&&(Ess(i)<=4*l1+3*l2)
        Ess(i)=arr6(2)*exp(-1j*n1*k*x(i));
    elseif (Ess(i)>4*l1+3*l2)&&(Ess(i)<=4*(l1+l2)+l4)
        Ess(i)=arr7(2)*exp(-1j*n2*k*x(i));
    elseif (Ess(i)>4*(l1+l2)+l4)&&(Ess(i)<=4*(l1+l2)+l4+l3)
        Ess(i)=arr8(2)*exp(-1j*n1*k*x(i));
    elseif (Ess(i)>4*(l1+l2)+l4+l3)&&(Ess(i)<=4*(l1+l2)+2*l4+l3)
        Ess(i)=arr9(2)*exp(-1j*n2*k*x(i));
    elseif (Ess(i)>4*(l1+l2)+2*l4+l3)&&(Ess(i)<=4*(l1+l2)+2*l4+2*l3)
        Ess(i)=arr10(2)*exp(-1j*n1*k*x(i));
    elseif (Ess(i)>4*(l1+l2)+2*l4+2*l3)&&(Ess(i)<=4*(l1+l2)+3*l4+2*l3)
        Ess(i)=arr11(2)*exp(-1j*n2*k*x(i));
    elseif (Ess(i)>4*(l1+l2)+3*l4+2*l3)&&(Ess(i)<=4*(l1+l2)+3*l4+3*l3)
        Ess(i)=arr12(2)*exp(-1j*n1*k*x(i));
    elseif (Ess(i)>4*(l1+l2)+3*l4+3*l3)&&(Ess(i)<=4*(l1+l2)+4*l4+3*l3)
        Ess(i)=arr13(2)*exp(-1j*n2*k*x(i));
    elseif (Ess(i)>4*(l1+l2)+4*l4+3*l3)&&(Ess(i)<=4*(l1+l2)+4*l4+4*l3)
        Ess(i)=arr14(2)*exp(-1j*n1*k*x(i));
    end
end
Ewave=abs(real(Ess));
yyaxis right
h2=plot(x*1e9,Ewave,Color="green",LineWidth=2,DisplayName="H component");
ylabel('The relative strength of the magnetic field')
hold on;
xlabel('coordinate/nm')
legend([h1,h2]);


function Mtrans=transcal(n,l)
lamd=1540e-9;
epsilon_0 = 8.854e-12;
mu_0 = 4*pi*1e-7; 
beta = (2*pi/lamd) * n * l;
p = sqrt(epsilon_0/mu_0) * n;
Mtrans = [cos(beta), -1j*sin(beta)/p; -1j*p*sin(beta), cos(beta)];
end
