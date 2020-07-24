# this exercise wants me to calculate the sum of three given numbers, but if the values are equal, then return
# three times their sum.

print("Enter three numbers to add together.")
print("If the numbers are all equal, the sum will be tripled.")

num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

num_sum = num1 + num2 + num3

if num1 == num2 == num3:
    print("\nValues are equal. Multiplying sum by 3.")
    num_sum *= 3

print(f"\nResult = {num_sum}")
