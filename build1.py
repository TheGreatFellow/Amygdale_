import numpy as np
import cv2
import datetime
t1 = datetime.datetime.now()
img = cv2.imread(r'C:\Users\S B Patil\Desktop\abcd.jpg') #<------just change the image location, nothing else
x_2d = img[:,:,0] #blue channel
y_2d = img[:,:,1] #green channel
z_2d = img[:,:,2] #red channel
arr=np.zeros([256,256,256], dtype = int)

#1


x = x_2d.flatten()
y = y_2d.flatten()
z = z_2d.flatten()

#2

dis = []
#3
for i in range(img.shape[0]*img.shape[1] - 1): 
         arr[z[i]][y[i]][x[i]] += 1
         dis.append(np.sqrt(np.power((int(z[i + 1]) - int(z[i])),2) + np.power((int(y[i + 1]) - int(y[i])),2) + np.power((int(x[i + 1]) - int(x[i])),2)))

print(arr.shape)
print("Image Dimension: " + str(img.shape[0]) + 'x' + str(img.shape[1]))
print("Total Sum: " + str(sum(dis)))
t2 = datetime.datetime.now()
print("Time taken for the Iteration: " + str(t2 - t1))

#(256, 256, 256)
#Image Dimension: 3456x5184
#Total Sum: 45043448.6450277
#Time taken for the Iteration: 0:03:06.291111