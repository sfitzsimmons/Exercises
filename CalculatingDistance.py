# this exercise aks me to take two sets of coordinates and compute the distance
import math

point1 = (4, 0)
point2 = (6, 6)

delta = abs(point1[0]-point2[0]), abs(point1[1] - point2[1])
distance = math.sqrt(delta[0]**2 + delta[1]**2)

print(round(distance, 2))
