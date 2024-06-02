%转移矩阵法求解1D光子晶体透射率及反射率
%转移矩阵
M=@(phi,ita) [cos(phi) -1i*sin(phi)/ita; -1i*ita*sin(phi) cos(phi)];
%参数
clear P
P.num=1e4; %计算点数
P.i=0; %入射角（弧度制）
P.n1=sqrt(5.5225); P.n2=sqrt(1.9044); %介质折射率
P.d1=740e-9; P.d2=1260e-9; %厚度/m
P.n0=1; P.n3=1; %两端折射率
P.nd=1.7; P.dd=1060e-9; %缺陷
P.c=3e8; %光速
P.mu0=4*pi*1e-7; %真空磁导率
P.omega0=P.c*pi/(P.n1*P.d1+P.n2*P.d2); %禁带基频
P=updateRange(P,0.5*P.omega0/P.c,5*P.omega0/P.c);

%% 查看透射率-波长关系
%周期10，正入射
N=10; %重复周期数
S=repmat([1,2],1,N); %结构矩阵，1代表介质1，2代表介质2，3代表缺陷
Data=PhC_1D_TMM_T(P,S,M);
plot1(creatAxes(P.i,N),P.wavelength,Data);

%%
%入射角45度
P.i=pi/4;
Data=PhC_1D_TMM_T(P,S,M);
plot1(creatAxes(P.i,N),P.wavelength,Data);

%周期5，正入射
N=5; P.i=0;
S=repmat([1,2],1,N);
Data=PhC_1D_TMM_T(P,S,M);
plot1(creatAxes(P.i,N),P.wavelength,Data);

%镜面对称缺陷，正入射
N=5; P.i=0;
S=[repmat([1,2],1,N),fliplr(repmat([1,2],1,N))];
Data=PhC_1D_TMM_T(P,S,M);
plot1(creatAxes(P.i,N,title='引入镜面对称缺陷，正入射'),P.wavelength,Data);

%% 查看透射率-角频率关系
P.num=1e5;
P=updateRange(P,0,6*P.omega0/P.c);
N=10; P.i=0;
S=repmat([1,2],1,N);
Data=PhC_1D_TMM_T(P,S,M);
ax=creatAxes(P.i,N,title='透射率-角频率，正入射');
plot1(ax,P.omega,Data);
xlabel(ax,"$\omega/\omega_0$","FontSize",15,Interpreter="latex")
%%
%引入单缺陷
S=[1,2,1,2,1,2,1,2,3,1,2,1,2,1,2,1,2];
Data=PhC_1D_TMM_T(P,S,M);
ax=creatAxes(P.i,N,title='透射率-角频率，正入射，中间引入单缺陷');
plot1(ax,P.omega,Data);
xlabel(ax,"$\omega/\omega_0$","FontSize",15,Interpreter="latex")
%% 一维双介质正入射能带
P.num=1e5;
P=updateRange(P,0,5*P.omega0/P.c);
Data=PhC_1D_TMM_T(P,inf,M);
ax=creatAxes(P.i,N,title='');
plot1(ax,Data,P.omega)
xlabel(ax,"$kD$","FontSize",15,Interpreter="latex")
ylabel(ax,"$\omega/\omega_0$","FontSize",15,Interpreter="latex")

%% 一些函数
function Data=PhC_1D_TMM_T(P,S,M)
    n10=P.n1/P.n0; n20=P.n2/P.n0; nd0=P.nd/P.n0; %相对折射率
    
    cosi0=cos(P.i); %入射角余弦
    cosi1=cos(asin(sin(P.i)/n10)); %介质2透射角余弦
    cosi2=cos(asin(sin(P.i)/n20));
    cosid=cos(asin(sin(P.i)/nd0));
    coe1=cosi1*P.d1;
    coe2=cosi2*P.d2;
    coed=cosid*P.dd;
    eta1=P.n1/P.c/P.mu0*cosi1; 
    eta2=P.n2/P.c/P.mu0*cosi2;
    etad=P.nd/P.c/P.mu0*cosid;
    p0=P.n0/P.mu0/P.c*cosi0; %入射区域参数
    p1=P.n3/P.mu0/P.c*cosi0; %出射区域参数
    Data=zeros(1,length(P.k)); %透射率

    for i=1:length(P.k)
        k0=P.k(i); k1=n10*k0; k2=n20*k0; kd=nd0*k0;
        phi1=k1*coe1; phi2=k2*coe2; phid=kd*coed;
        
        %介质的转移矩阵
        Ms(:,:,1)=M(phi1,eta1); 
        Ms(:,:,2)=M(phi2,eta2); 
        Ms(:,:,3)=M(phid,etad); %缺陷

        if S==inf
            % 计算一维双介质正入射能带
            Data(i)=real(acos(cos(phi1)*cos(phi2)-0.5*(eta1/eta2+eta2/eta1)*sin(phi1)*sin(phi2)));
        else
            M0=eye(2);
            for n=S
                M0=M0*Ms(:,:,n);
            end
            Data(i)=abs(2*p0/(p0*(M0(1,1)+M0(1,2)*p1)+M0(2,1)+M0(2,2)*p1))^2; %透射率
        end
    end
end

function a=creatAxes(i1,N,varargin)
    %检测是否要改变标题
    p=inputParser;
    addParameter(p,'title',['透射率-波长（i=',num2str(i1*180/pi),'°,N=',num2str(N),'）']);
    parse(p,varargin{:});
    t=p.Results.title;
    figure(Color='w')
    a=axes;
    title(a,t,"FontSize",15)
    xlabel(a,"波长(nm)","FontSize",15); ylabel(a,"透射率","FontSize",15)
    axis(a,"tight"); hold(a,"on")
end

function plot1(ax,x,y)
    plot(ax,x,y,LineWidth=1.5)
    hold(ax,"off")
end

function P=updateRange(P,mink,maxk)
    P.k=linspace(mink,maxk,P.num); %波矢
    P.wavelength=2*pi*1e9./P.k; %入射光波长范围/nm
    P.omega=P.k*P.c/P.omega0; %以禁带基频为单位的频率(真空中)
end