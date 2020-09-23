import numpy as np
import cv2
import datetime
np.seterr(divide='ignore', invalid='ignore')

t1 = datetime.datetime.now()
img = cv2.imread(r'C:\Users\S B Patil\Desktop\EXP\Amygdale\abcd.jpg') #<------just change the image location, nothing else
x_2d = img[:,:,0] #blue channel
y_2d = img[:,:,1] #green channel
z_2d = img[:,:,2] #red channel

A = img.reshape(img.shape[0]*img.shape[1],3)
print(len(A))
z = np.zeros([1, 3], dtype = int)
A1 = np.vstack((A,z))
A2 = np.vstack((z, A))

CompArr = A1==A2
TruArr = np.matrix([True,True,True])
sum1 = sum(CompArr == TruArr)
print(sum1)