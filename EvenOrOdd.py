# this exercise wants me to write a program that determines whether a number is even or odd.


def even_or_odd(num):
    if num % 2 == 1:
        print("This number is odd.")
    else:
        print("This number is even.")


even_or_odd(int(input("Enter number: ")))
