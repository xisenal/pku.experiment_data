%设置参数：
tau=0.33;
m_b=0.106*10^(-3);
mu_0=0.000549;
a_num=0.2;
eta=m_b/(mu_0*a_num);
F_T=8.93;
N=6;
%求解
f=linspace(0,1000,100000);
deltas=2*pi*sqrt(mu_0*(f.^2)*a_num^2/F_T);
nope=[];
for delta=deltas
    M=[1 0;-eta*delta 1];
    phi=[0;1];
    phi=Tran(delta*(1-tau))*M*Tran(delta*tau)*phi;
    for j=2:N
        phi=Tran(delta*(j-tau-floor(j-tau)))*M*Tran(delta*(floor(j-tau)-j+tau+1))*phi;
    end
    nope(end+1)=phi(1);
end
figure(1)
plot(f,nope)
ansf=[];
for i=1:numel(nope)-1
    if nope(i)*nope(i+1)<=0
        if abs(nope(i))>=abs(nope(i+1))
            ansf(end+1)=f(i+1);
        else
            ansf(end+1)=f(i);
        end
    end
end
ansf=ansf(2:end);
for i=1:numel(ansf)
    disp(i)
    disp(ansf(i))
end














function T=Tran(phi)
    T=[cos(phi) sin(phi);-sin(phi) cos(phi)];
end