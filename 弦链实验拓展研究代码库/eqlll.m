l1=0.06;
l2=0.24;
eps1=1;
eps2=36;
a=l1+l2;
numG=4;
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
for k=-pi/a:0.002*pi/a:pi/a
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

disp(dispe)

