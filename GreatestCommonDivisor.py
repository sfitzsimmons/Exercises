# this exercise asks me to create a program to find the greatest common divisor of two integers.

int1 = int(input("Enter first integer: "))
int2 = int(input("Enter second integer: "))


def greatest_common_divisor(x, y):
    gcd = 1
    for k in range(int(int1/2), 0, -1):
        if int1 % k == 0 and int2 % k == 0:
            gcd = k
            break
    return gcd


print(f"The greatest common divisor of {int1} and {int2} = ", greatest_common_divisor(int1, int2))

