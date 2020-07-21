# This exercise aks to calculate the volume of a sphere

import math

radius = float(input("Enter radius of sphere: "))


def sphere_volume(rad):
    volume = 4/3 * math.pi ** 3
    return round(volume, 4)


print(f"The volume of the sphere is {sphere_volume(radius)}")
