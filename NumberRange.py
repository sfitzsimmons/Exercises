# this exercise wants me to test whether a number is within 100 of 1000 or 2000.

given_number = int(input("Enter number: "))

if 900 < given_number < 1100:
    print("Your number is within 100 of 1000.")
elif 1900 < given_number < 2100:
    print("Your number is within 100 of 2000")
else:
    print("Your number is not within 100 of 1000 or 2000.")
