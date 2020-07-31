# this exercise asks for me to return the sum of two numbers, but if the sum equals between 15 and 20, return 20.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


def num_sum(x, y):
    if 20 >= num1 + num2 >= 15:
        return 20
    else:
        return num1 + num2


print(num_sum(num1, num2))
