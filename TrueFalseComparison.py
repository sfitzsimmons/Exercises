# this exercise asks me to return true if two numbers are equal or their sum or difference equals 5.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


def num_comparitor(x, y):
    if x == y:
        return True
    elif abs(x - y) == 5:
        return True
    elif x + y == 5:
        return True
    else:
        return False


print(num_comparitor(num1, num2))

