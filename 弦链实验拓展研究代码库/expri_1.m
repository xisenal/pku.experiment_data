M = [1 2 3; 4 5 6; 7 8 9];
% 仅计算特征值
eigenvalues = eig(M);
disp('Eigenvalues:');
disp(eigenvalues);
% 计算特征值和特征向量
% [V, D] = eig(M);
% disp('Eigenvectors:');
% disp(V);
% disp('Diagonal matrix of eigenvalues:');
% disp(D);
