# this exercise asks for me to take three integers and return their sum, but if 2 of the integers are equal, return 0.

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))


def three_num_sum(x, y, z):
    if x == y or x == z or y == z:
        return 0
    else:
        return x + y + z


print(three_num_sum(num1, num2, num3))
