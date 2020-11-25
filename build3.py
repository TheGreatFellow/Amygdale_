import numpy as np
import cv2
import datetime
import statistics
import matplotlib.pyplot as plt
np.seterr(divide='ignore', invalid='ignore')
t1 = datetime.datetime.now()
img = cv2.imread(r'..\720img.jpg') #<------just change the image location, nothing else(it reads the image)
x_2d = img[:,:,0] #blue channel
y_2d = img[:,:,1] #green channel
z_2d = img[:,:,2] #red channel

arr=np.zeros([256,256,256], dtype = int) # initializing array of zeroes 

nos = range(256)

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
vec_x = (x_1 - x)/abs(x_1 - x)
vec_y = (y_1 - y)/abs(y_1 - y)
vec_z = (z_1 - z)/abs(z_1 - z)
vec_x[np.isnan(vec_x)] = 0
vec_y[np.isnan(vec_y)] = 0
vec_z[np.isnan(vec_z)] = 0

# Variance Model

var_x = [ [] for _ in range(256)]
var_y = [ [] for _ in range(256)]
var_z = [ [] for _ in range(256)]
mean_x = [0] * 256
mean_y = [0] * 256
mean_z = [0] * 256


# Plots the RGB values on 255x255x255 grid
for i in range(img.shape[0] * img.shape[1]): 
         arr[z[i]][y[i]][x[i]] += 1
         if x_1[i] not in var_x[x[i]]:
            var_x[x[i]].append(x_1[i])
         if y_1[i] not in var_y[y[i]]:
            var_y[y[i]].append(y_1[i])
         if z_1[i] not in var_z[z[i]]:
            var_z[z[i]].append(z_1[i])

for i in range(256):
   if not var_x[i]:
       mean_x[i] = 0
   else:
       mean_x[i] = statistics.mean(var_x[i])

   if not var_y[i]:
       mean_y[i] = 0
   else: 
       mean_y[i] = statistics.mean(var_y[i])

   if not var_z[i]:
       mean_z[i] = 0
   else: 
       mean_z[i] = statistics.mean(var_z[i])


t2 = datetime.datetime.now()

plt.plot(mean_x, label = "Mean")
# plt.plot(dis, label = "Distance")
plt.show()
print(arr.shape)
print("Image Dimension: " + str(img.shape[0]) + 'x' + str(img.shape[1]))
print("Time taken for the Iteration: " + str(t2 - t1))


# Image Dimension: 3456x5184
# Total Sum: 45043506.954546645
# Time taken for the Iteration: 0:00:58.518444 