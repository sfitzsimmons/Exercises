# this exercise asks for me to calculate the least common multiple of 2 positive integers.


def least_common_multiple(x,y):
    x_list = []
    y_list = []
    lcm = 0

    for k in range(1, y):
        x_list.append(x*k)
    for k in range(1, x):
        y_list.append(y*k)

    for multiple in x_list:
        if multiple in y_list:
            lcm = multiple
            break
    return lcm


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"The least common multiple of {num1} and {num2} = ", least_common_multiple(num1, num2))
