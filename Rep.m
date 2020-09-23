X = double(imread('C:\Users\S B Patil\Desktop\EXP\Amygdale\abcd.jpg')); %add your own image
img_size = size(X);

% Reshape the image into an Nx3 matrix where N = number of pixels.
% Each row will contain the Red, Green and Blue pixel values
A = reshape(X, img_size(1) * img_size(2), 3);
 
n=0; j=0;

A1 = [A(1000:1100,:);zeros(1,3)];
A2 = [zeros(1,3);A(1000:1100,:)];
C = (A1 == A2);
%disp(A1);
%disp(A2);
%disp(C);


A_mean = mean(A');
A_var = var(A');
 
