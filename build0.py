import numpy as np
import cv2
import matplotlib.pyplot as plt
import mpl_toolkits.axes_grid1
from mpl_toolkits import mplot3d
import random
from itertools import product
import datetime
img = cv2.imread(r'C:\Users\S B Patil\Desktop\abcd.jpg') #<------just change the image location, nothing else
x_2d = img[:,:,0] #blue channel
y_2d = img[:,:,1] #green channel
z_2d = img[:,:,2] #red channel
arr=np.zeros([256,256,256], dtype = int)

#1
t1 = datetime.datetime.now()
         
#2


#3
j = 0
for i in range(img.shape[0]):
     for j in range(img.shape[1]):
         arr[z_2d[i][j]][y_2d[i][j]][x_2d[i][j]] += 1

t2 = datetime.datetime.now()
print(arr)
print(arr.shape)
print("Image Dimension: " + str(img.shape[0]) + 'x'+str(img.shape[1]))
print("Time taken for the Iteration: " + str(t2 - t1))