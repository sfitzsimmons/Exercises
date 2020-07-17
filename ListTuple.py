# this exercise asks to take a sequence of comma separated numbers and to turn them into a list and a tuple

user_input = (input("Enter your comma separated numbers: "))

# to make it so every character isn't taken as a list entry I need to use the .split() method to separate by commas
l1 = list(user_input.split(","))

# I can just convert the list into a tuple
t1 = tuple(l1)

print(l1)
print(t1)

