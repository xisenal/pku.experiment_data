%先建立介电常数变换后的矩阵 
a=1e-6;
r=0.4*a;
eps1=9;
eps2=1;
precis=5;
nG=4;
precisStruct=30;
nx=1;
for countX=-a/2:a/precisStruct:a/2
    ny=1;
    for countY=-a/2:a/precisStruct:a/2
        if(sqrt(countX^2+countY^2)<r)
            struct(nx,ny)=1/eps2;
            xSet(nx)=countX;
            ySet(ny)=countY;
        else
            struct(nx,ny)=1/eps1;
            xSet(nx)=countX;
            ySet(ny)=countY;
        end
        ny=ny+1;
    end
    nx=nx+1;
end
dS=(a/precisStruct)^2;
xMesh=meshgrid(xSet(1:length(xSet)-1));
yMesh=meshgrid(ySet(1:length(ySet)-1))';
structMesh=struct(1:length(xSet)-1,...
1:length(ySet)-1)*dS/(max(xSet)-min(xSet))^2;
kx(1:precis+1)=0:pi/a/precis:pi/a;
ky(1:precis+1)=zeros(1,precis+1);
kx(precis+2:precis+precis+1)=pi/a;
ky(precis+2:precis+precis+1)=...
pi/a/precis:pi/a/precis:pi/a;
kx(precis+2+precis:precis+precis+1+precis)=...
pi/a-pi/a/precis:-pi/a/precis:0;
ky(precis+2+precis:precis+precis+1+precis)=...
pi/a-pi/a/precis:-pi/a/precis:0;
numG=1;
for Gx=-nG*2*pi/a:2*pi/a:nG*2*pi/a
    for Gy=-nG*2*pi/a:2*pi/a:nG*2*pi/a
        G(numG,1)=Gx;
        G(numG,2)=Gy;
        numG=numG+1;
    end
end
for countG=1:numG-1
    for countG1=1:numG-1
        CN2D_N(countG,countG1)=sum(sum(structMesh.*...
        exp(1i*((G(countG,1)-G(countG1,1))*...
        xMesh+(G(countG,2)-G(countG1,2))*yMesh))));
    end
end
for countG=1:numG-1
    for countG1=1:numG-1
        for countK=1:length(kx)
            M(countK,countG,countG1)=...
            CN2D_N(countG,countG1)*((kx(countK)+G(countG1,1))*...
            (kx(countK)+G(countG1,1))+...
            (ky(countK)+G(countG1,2))*(ky(countK)+G(countG1,2)));
        end
    end
end
for countK=1:length(kx)
    MM(:,:)=M(countK,:,:);
    [D V]=eig(MM);
    dispe(:,countK)=sqrt(V*ones(length(V),1))*a/2/pi;
end
figure(3);
ax1=axes;
hold on;
for u=1:8
plot(abs(dispe(u,:)),'r','LineWidth',1.5);
if(min(dispe(u+1,:))>max(dispe(u,:)))
rectangle('Position',[1,max(dispe(u,:)),...
length(kx)-1,min(dispe(u+1,:))-...
max(dispe(u,:))],'FaceColor','b',...
'EdgeColor','b');
end
end
set(ax1,'xtick',...
[1 precis+1 2*precis+1 3*precis+1]);
set(ax1,'xticklabel',['G';'X';'M';'G']);
ylabel('Frequency \omegaa/2\pic','FontSize',12);
xlabel('Wavevector','FontSize',12);
xlim([1 16])
set(ax1,'XGrid','on');