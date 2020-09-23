import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import mpl_toolkits.axes_grid1
import random
import datetime
figure = plt.figure()
axis = mpl_toolkits.mplot3d.Axes3D(figure)
no_of_pints = int(input("specify the number of random points you need: "))
# points = [i for  i in range(no_of_pints + 1)]
# point = 1
# while point <= no_of_pints:
    # points[point] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    # print(points[point])
    # point = point + 1
point = 0
x_coordinates = [0 for  i in range(no_of_pints + 1)]
y_coordinates = [0 for  i in range(no_of_pints + 1)]
z_coordinates = [0 for  i in range(no_of_pints + 1)]

while point <= no_of_pints:
    x_coordinates[point] =  random.randint(0, 255)
    y_coordinates[point] =  random.randint(0, 255)
    z_coordinates[point] =  random.randint(0, 255)
    point += 1
import open    
axis.scatter(x_coordinates, y_coordinates, z_coordinates)
dis = []
total_dis = 0
t1 = datetime.datetime.now()
for i in range(0, no_of_pints):
    for j in range(0, no_of_pints):
            #dis_x = 0
            dis_x = np.power(x_coordinates[i] - x_coordinates[j],2)
            #dis_y = 0
            dis_y = np.power(y_coordinates[i] - y_coordinates[j],2)
            #dis_z = 0
            dis_z = np.power(z_coordinates[i] - z_coordinates[j],2)
            dis.append(np.sqrt(dis_x+dis_y+dis_z))

t2 = datetime.datetime.now()
print(t2-t1)
plt.show(figure)
