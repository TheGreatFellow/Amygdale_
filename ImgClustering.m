A = double(imread('C:\Users\S B Patil\Desktop\EXP\Amygdale\abcd.jpg')); %add your own image
img_size = size(A);

% Reshape the image into an Nx3 matrix where N = number of pixels.
% Each row will contain the Red, Green and Blue pixel values
X = reshape(A, img_size(1) * img_size(2), 3);
l1 = img_size(1); %number of pixels aka length

[L,centers] = kmeans(X,7);

l = length(centers); k = 0;
for i = 1:l
  disp(sum(L==i));
  k+= sum(L==i);
endfor
disp(k);disp(centers);