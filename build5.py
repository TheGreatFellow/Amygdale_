import numpy as np
import cv2
import datetime
import statistics
import matplotlib.pyplot as plt
import itertools
np.seterr(divide='ignore', invalid='ignore')
t1 = datetime.datetime.now()
# <------just change the image location, nothing else(it reads the image)
img = cv2.imread(r'..\1080img.jpg')
z_2d = img[:, :, 0]  # blue channel
y_2d = img[:, :, 1]  # green channel
x_2d = img[:, :, 2]  # red channel

arr = [[['0' for col in range(256)] for col in range(256)]
       for row in range(256)]  # initializing array of zeroes
x = (x_2d.flatten()).astype(int)
y = (y_2d.flatten()).astype(int)
z = (z_2d.flatten()).astype(int)
rgb_3 = list(zip(x, y, z))
rep_uniq = [k for k, g in itertools.groupby(rgb_3)]
count_dupe = [sum(1 for _ in group) for _, group in itertools.groupby(rgb_3)]
x_u = [a for a, b, c in rep_uniq]
y_u = [b for a, b, c in rep_uniq]
z_u = [c for a, b, c in rep_uniq]
p = count_dupe.index(max(count_dupe))

# Distance Calculation
dis = []
x_1 = np.delete(np.append(x_u, x_u[0]), 0)
y_1 = np.delete(np.append(y_u, y_u[0]), 0)
z_1 = np.delete(np.append(z_u, z_u[0]), 0)
dis = (np.sqrt((x_1 - x_u)**2 + (y_1 - y_u)**2 + (z_1 - z_u)**2))

# Vector Calculation
vec_x = (x_1 - x_u)/abs(x_1 - x_u)
vec_y = (y_1 - y_u)/abs(y_1 - y_u)
vec_z = (z_1 - z_u)/abs(z_1 - z_u)
vec_x[np.isnan(vec_x)] = 1
vec_y[np.isnan(vec_y)] = 1
vec_z[np.isnan(vec_z)] = 1
vec_x = [int(i) for i in vec_x]
vec_y = [int(i) for i in vec_y]
vec_z = [int(i) for i in vec_z]

# Variance Model
var_x = [[] for _ in range(256)]
var_y = [[] for _ in range(256)]
var_z = [[] for _ in range(256)]
mean_x = [0] * 256
mean_y = [0] * 256
mean_z = [0] * 256


# Plots the RGB values on 255x255x255 grid
for i in range(len(rep_uniq)):
    if arr[x_u[i]][y_u[i]][z_u[i]] == '0':
        arr[x_u[i]][y_u[i]][z_u[i]] = '1'
    tem = ''
    if count_dupe[i] > 1:
        tem += '1'
        tem += str(count_dupe[i])
    else:
        tem += '0'
    tem += str(vec_x[i]) + str(vec_y[i]) + str(vec_z[i])
    arr[x_u[i]][y_u[i]][z_u[i]] += tem
    if x_1[i] not in var_x[x_u[i]]:
        var_x[x_u[i]].append(x_1[i])
    if y_1[i] not in var_y[y_u[i]]:
        var_y[y_u[i]].append(y_1[i])
    if z_1[i] not in var_z[z_u[i]]:
        var_z[z_u[i]].append(z_1[i])

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

# plt.plot(mean_x, label = "Blue")
# plt.plot(mean_y, label = "Green")
# plt.plot(var_x, label = "Red")
# plt.plot(dis, label = "Distance")
# plt.show()
print("\nThe supposed \"Binary code\" for the RGB colour which repeats maximum number of times consecutively: " +
      arr[x_u[p]][y_u[p]][z_u[p]])
# np.savetxt('arrta.txt', [arr.flatten()], delimiter='', fmt='%s', newline="\n")
# print(arr)
print("\nImage Dimension: " + str(img.shape[0]) + 'x' + str(img.shape[1]))
print("Time taken for the Iteration: " + str(t2 - t1))


# Image Dimension: 781x380
# Time taken for the Iteration: 0:00:02.855424

# Image Dimension: 1080x1920
# Time taken for the Iteration: 0:00:13.683899
