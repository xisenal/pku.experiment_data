l1=0.24;
l2=0.06;
eps1=1;
eps2=36;
a=l1+l2;
numG=500;
count_k=0;
countG=1;
countG1=1;
chi = zeros((2*numG+1), (2*numG+1)); 
M=chi;
ME=chi;
ks=zeros(1,11);
dispe=zeros(11,(2*numG+1));
dispeE=dispe;
for G=-numG*2*pi/a:2*pi/a:numG*2*pi/a 
    for G1=-numG*2*pi/a:2*pi/a:numG*2*pi/a
        if (G-G1)==0
            chi(countG1,countG)=1/(l1+l2)*(1/eps1*l1+1/eps2*l2);
        else
            chi(countG1,countG)=1i/(l1+l2)/(G-G1)*...
            (1/eps1*(exp(-1i* (G-G1)*l1)-1)+1/eps2*...
            (exp(-1i* (G-G1)*(l1+l2))-exp(-1i* (G-G1)*l1)));
        end
    countG=countG+1;
    end
    countG1=countG1+1;
    countG=1;
end
countG=1;
countG1=1;
for k=-pi/a:0.25*pi/a:pi/a
    for G=-numG*2*pi/a:2*pi/a:numG*2*pi/a %G
        for G1=-numG*2*pi/a:2*pi/a:numG*2*pi/a %G’
            M(countG1,countG)=chi(countG1,countG)*(k+G1)*(k+G1);
            % ME(countG1,countG)=chi(countG1,countG)*(k+G1)*(k+G);
            countG=countG+1;
        end
        countG1=countG1+1;
        countG=1;
    end
    countG1=1;
    V=eig(M);
    % VE=eig(ME);
    count_k=count_k+1;
    dispe(count_k,:)=sqrt(sort(abs(V)))*20.62;
    %*a/2/pi
    % dispeE(count_k,:)=sqrt((sort(abs(VE))))*a/2/pi;
    ks(count_k)=k;
end
ks=ks*a;
figure(1);
hold on;
for u=1:6
    plot(ks,dispe(:,u),"Color",'red','LineWidth',2);
    hold on;
end

xline(0,'b--',Linewidth=1.5)
hold on;
xline(pi/4,'b--',Linewidth=1.5)
hold on;
xline(2*pi/4,'b--',Linewidth=1.5)
hold on;
xline(3*pi/4,'b--',Linewidth=1.5)
hold on;
xline(pi,'b--',Linewidth=1.5)
hold on;
xline(-pi/4,'b--',Linewidth=1.5)
hold on;
xline(-2*pi/4,'b--',Linewidth=1.5)
hold on;
xline(-3*pi/4,'b--',Linewidth=1.5)
hold on;
xline(-pi,'b--',Linewidth=1.5)
hold on;
% title("the band structure of TM wave")
% xlabel('\kappaa');
% ylabel('\omega_r=\omegaa/2\pic');
title("Equivalent photonic crystal band diagram")
xlabel("\kappaa")
ylabel("f/Hz")
xlim([-pi , pi]);
% xlim([-pi/a pi/a]);
