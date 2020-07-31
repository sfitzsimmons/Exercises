# this exercise wants me to print the colors from the first list that aren't contained in the second list

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

# expected output: {'Black', 'White'}

color_list = []

for color in color_list_1:
    if color not in color_list_2:
        color_list.append(color)
    else:
        pass

print(color_list)
