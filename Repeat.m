A = double(imread('C:\Users\S B Patil\Desktop\abcd.jpg')); %add your own image
img_size = size(A);

% Reshape the image into an Nx3 matrix where N = number of pixels.
% Each row will contain the Red, Green and Blue pixel values
X = reshape(A, img_size(1) * img_size(2), 3);
l = img_size(1); %number of pixels aka length

n=0; j=0;

reppixels = []; %matrix to store which pixel repeats how many times

for i = 1:(l-1)
  if(X(i,:) == X(i+1,:)  &&  i>1)
      j++;
  elseif(X(i,:) != X(i+1,:)  &&  i>1)
      n = n + j;
      if(j>0)
      reppixels = [reppixels;X(i,:),j];
      endif
      j=0;
  endif
  i++;
endfor

disp(n); disp(size(X));
disp(reppixels);
