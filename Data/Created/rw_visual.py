import matplotlib.pyplot as plt

from random_walk import RandomWalk

#take a walk
rw= RandomWalk()
rw.fill_walk()

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=15)

#Emphasize starting and end points
plt.scatter(0,0,c='green',s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',s=100)
plt.show()
