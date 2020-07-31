# this exercise asks for me to compare two numbers and return true if they're equal or 5 apart.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


def number_comparitor(x, y):
    if x == y or x + y == 5 or abs(x - y) == 5:
        return True
    else:
        return False


print(number_comparitor(num1, num2))

