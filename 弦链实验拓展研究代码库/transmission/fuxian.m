[T_f1,lbd1] = calculate_transmission(4,680e-9,815e-9,2.82^2,1.46^2);
[T_f2,lbd2] = calculate_transmission(4,685e-9,1290e-9,2.82^2,1.46^2);

plot(lbd1,T_f1,LineWidth=2,DisplayName='PhC 1');
hold on;
plot(lbd2,T_f2,LineWidth=2,DisplayName='PhC 2');
title('Transmission vs Frequency');
xlabel('Frequency (Hz)');
ylabel('Transmission');
legend;
grid on;

function [T_f,lbd] = calculate_transmission(N, l1, l2, e1, e2)
    epsilon_0 = 8.854e-12;
    mu_0 = 4*pi*1e-7; 
    % 设置频谱范围
    fre = linspace(1e14, 2.5e14, 100000);
    c = 3e8;
    % 求出单周期特征矩阵，正入射假设下
    n1 = sqrt(e1);
    n2 = sqrt(e2);
    lbd = c ./ fre;
    lbd = flip(lbd);
    T_f = zeros(size(lbd));
    i = 1;
    for lamd = lbd
        beta1 = (2*pi/lamd) * n1 * l1;
        beta2 = (2*pi/lamd) * n2 * l2;
        p1 = sqrt(epsilon_0/mu_0) * n1;
        p2 = sqrt(epsilon_0/mu_0) * n2;
        p0 = sqrt(epsilon_0/mu_0);
        
        M_of1 = [cos(beta1), -1j*sin(beta1)/p1; -1j*p1*sin(beta1), cos(beta1)];
        M_of2 = [cos(beta2), -1j*sin(beta2)/p2; -1j*p2*sin(beta2), cos(beta2)];
        M_of_period = M_of1 * M_of2;
        
        % 初始化M_form为单位矩阵
        M_form = eye(2);
        % 使用循环逐步相乘，以提高数值稳定性
        for k = 1:N
            M_form = M_form * M_of_period;
        end
        
        Trans = (2*p0) / ((M_form(1,1) + M_form(1,2) * p1) * p0 + (M_form(2,1) + M_form(2,2) * p1));
        Trans = abs(Trans)^2;
        T_f(i) = Trans;
        i = i + 1;
    end
end