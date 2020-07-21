# This exercise wants me to write a program that prints the first and last colors from a given list

color_list = ["Red", "Green", "White", "Black"]

print(color_list[0], color_list[-1])

# 2 more ways

colors = [color_list[0], color_list[-1]]

print(colors)

for color in color_list:
    if color == color_list[0] or color == color_list[-1]:
        print(color)
