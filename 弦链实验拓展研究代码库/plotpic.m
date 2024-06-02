%晶体图
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
for k=-pi/a:0.1*pi/a:pi/a
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
for u=1:3
    plot(ks,dispe(:,u),"Color",'c','LineWidth',2,DisplayName="Equivalent PhC's band structure");
    hold on;
end
h4=plot(ks,dispe(:,4),"Color",'c','LineWidth',2,DisplayName="Equivalent PhC's band structure");


    tau = 0.5;
    m_b = 0.114 * 10^(-3);
    mu_0 = 0.000549;
    a_num = 0.3;
    mu_1 = 36 * mu_0;
    F_T = 8.93;
    N = 100;
    f = linspace(0, 1000, 100000);
    deltas1 = 2 * pi * sqrt(mu_1 * f.^2 * a_num^2 / F_T);
    deltas2 = 2 * pi * sqrt(mu_0 * f.^2 * a_num^2 / F_T);
    nope = [];
    
    for j = 2:length(f) % MATLAB 索引从 1 开始
        delta1 = deltas1(j);
        delta2 = deltas2(j);
        phi = [0; 1];
        
        for i = 1:N
            phi = T_mesh(delta1 * 0.2) * phi;
            phi(2) = phi(2) * delta1 / delta2;
            phi = T_mesh(delta2 * (1 - 0.2)) * phi;
            phi(2) = phi(2) * delta2 / delta1;
        end
        
        nope = [nope, phi(1)];
    end
    
    ans_f = [];
    for i = 1:length(nope) - 1
        if nope(i) * nope(i + 1) <= 0
            ans_f = [ans_f, f(i)];
        end
    end
    
    xlss = linspace(pi / N, (1 - 1 / N)*pi, N - 1);
    xrss = flip(xlss);
    
    plot(xlss, ans_f(1:N-1),Color="m",LineWidth=1.5);
    hold on;
    plot(-xlss, ans_f(1:N-1),Color="m",LineWidth=1.5);
    hold on;
    plot(xrss, ans_f(N+1:N*2-1),Color="m",LineWidth=1.5);
    hold on;
    plot(-xrss, ans_f(N+1:N*2-1),Color="m",LineWidth=1.5);
    hold on;
    plot(xlss, ans_f(N*2+1:N*3-1),Color="m",LineWidth=1.5);
    hold on;
    h3=plot(-xlss, ans_f(N*2+1:N*3-1),Color="m",LineWidth=1.5,DisplayName="String Chain Theory Model");
    hold on;
    plot(xrss, ans_f(3*N+1:N*4-1),Color="m",LineWidth=1.5);
    hold on;
    plot(-xrss, ans_f(3*N+1:N*4-1),Color="m",LineWidth=1.5);
    hold on;

% xline(0,'b--',Linewidth=1.5)
% hold on;
% xline(pi/4,'b--',Linewidth=1.5)
% hold on;
% xline(2*pi/4,'b--',Linewidth=1.5)
% hold on;
% xline(3*pi/4,'b--',Linewidth=1.5)
% hold on;
% xline(pi,'b--',Linewidth=1.5)
% hold on;
% xline(-pi/4,'b--',Linewidth=1.5)
% hold on;
% xline(-2*pi/4,'b--',Linewidth=1.5)
% hold on;
% xline(-3*pi/4,'b--',Linewidth=1.5)
% hold on;
% h2=xline(-pi,'b--',Linewidth=1.5,DisplayName="Brillouin zone boundary");
% hold on;




h1=errorbar(pi/4, 18.87, 3, 'ro', 'MarkerSize', 4, 'MarkerFaceColor', 'r',DisplayName="Experimental value");
errorbar(2*pi/4, 36.08, 3, 'ro', 'MarkerSize', 4, 'MarkerFaceColor', 'r');
errorbar(3*pi/4, 48.87, 3, 'ro', 'MarkerSize', 4, 'MarkerFaceColor', 'r');
errorbar(4*pi/4, 93.33, 4, 'ro', 'MarkerSize', 4, 'MarkerFaceColor', 'r');
errorbar(3*pi/4, 159.30, 4, 'ro', 'MarkerSize', 4, 'MarkerFaceColor', 'r');
errorbar(2*pi/4, 169.98, 4, 'ro', 'MarkerSize', 4, 'MarkerFaceColor', 'r');
errorbar(pi/4, 183.42, 6, 'ro', 'MarkerSize', 4, 'MarkerFaceColor', 'r');
errorbar(0, 242.98, 6, 'ro', 'MarkerSize', 4, 'MarkerFaceColor', 'r');
errorbar(1*pi/4,257.15 ,10 , 'ro', 'MarkerSize', 4, 'MarkerFaceColor', 'r');
errorbar(2*pi/4, 269.34, 10, 'ro', 'MarkerSize', 4, 'MarkerFaceColor', 'r');
errorbar(3*pi/4, 282.12, 10, 'ro', 'MarkerSize', 4, 'MarkerFaceColor', 'r');
errorbar(4*pi/4, 291.93, 8, 'ro', 'MarkerSize', 4, 'MarkerFaceColor', 'r');
errorbar(3*pi/4, 358.12, 9, 'ro', 'MarkerSize', 4, 'MarkerFaceColor', 'r');
errorbar(2*pi/4, 366.65, 10, 'ro', 'MarkerSize', 4, 'MarkerFaceColor', 'r');
errorbar(1*pi/4, 378.23, 11, 'ro', 'MarkerSize', 4, 'MarkerFaceColor', 'r');

h.LineWidth = 2;



xlabel("\kappaa")
ylabel("f/Hz")
title("Experimental value, theoretical value, corresponding value")
legend([h1,h3,h4]);
grid on;








function A = T_mesh(p)
    A = [cos(p), sin(p); -sin(p), cos(p)];
end

