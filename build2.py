import numpy as np
import cv2
import datetime
np.seterr(divide='ignore', invalid='ignore')
t1 = datetime.datetime.now()
# <------just change the image location, nothing else(it reads the image)
img = cv2.imread(r'..\8kexp.jpg')
x_2d = img[:, :, 0]  # blue channel
y_2d = img[:, :, 1]  # green channel
z_2d = img[:, :, 2]  # red channel

arr = np.zeros([256, 256, 256], dtype=int)  # initializing array of zeroes


x = (x_2d.flatten()).astype(int)
y = (y_2d.flatten()).astype(int)
z = (z_2d.flatten()).astype(int)


# Distance Calculation
dis = []
x_1 = np.delete(np.append(x, x[0]), 0)
y_1 = np.delete(np.append(y, y[0]), 0)
z_1 = np.delete(np.append(z, z[0]), 0)
dis = (np.sqrt((x_1 - x)**2 + (y_1 - y)**2 + (z_1 - z)**2))

# Vector Calculation
vectorx = (x_1 - x)/abs(x_1 - x)
vectory = (y_1 - y)/abs(y_1 - y)
vectorz = (z_1 - z)/abs(z_1 - z)

# Plots the RGB values on 255x255x255 grid
for i in range(img.shape[0] * img.shape[1]):
    arr[z[i]][y[i]][x[i]] += 1


t2 = datetime.datetime.now()
print(arr.shape)
print("Image Dimension: " + str(img.shape[0]) + 'x' + str(img.shape[1]))
print("Total Sum: " + str(sum(dis)))
print("Time taken for the Iteration: " + str(t2 - t1))


# Image Dimension: 3456x5184
# Total Sum: 45043506.954546645
# Time taken for the Iteration: 0:00:31.561279
#####################################################
# Image Dimension: 4384x6576
# Total Sum: 221359503.056713
# Time taken for the Iteration: 0:00:51.253434
