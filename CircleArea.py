# Write out a Python program which accepts the radius of a circle from the user and computes the area
import math


def circle_area():
    radius = float(input("Enter radius: "))
    return math.pi * radius ** 2


# I decided to use the round function to make it look nice.
print("Your circle has an area of: ", round(circle_area(), 3))
