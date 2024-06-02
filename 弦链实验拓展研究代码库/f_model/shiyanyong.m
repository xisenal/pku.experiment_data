
    tau = 0;
    m_b = 0.114 * 10^(-3);
    mu_0 = 0.000549;
    a_num = 0.3;
    mu_1 = 36 * mu_0;
    F_T = 8.93;
    N = 100;
    f = linspace(0, 1000, 100000);
    deltas1 = 2 * pi * sqrt(mu_0 * f.^2 * a_num^2 / F_T);
    deltas2 = 2 * pi * sqrt(mu_1 * f.^2 * a_num^2 / F_T);
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
    
    figure;
    hold on;
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
    plot(-xlss, ans_f(N*2+1:N*3-1),Color="m",LineWidth=1.5);
    hold on;


function A = T_mesh(p)
    A = [cos(p), sin(p); -sin(p), cos(p)];
end
