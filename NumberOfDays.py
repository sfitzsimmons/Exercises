# This exercise asks me to calculate the number of days between two dates using the datetime module

import datetime

# first, get the dates from the user

print("Enter first date")
y1 = int(input("Year: "))
m1 = int(input("Month: "))
d1 = int(input("Day: "))

print("\nEnter second date")
y2 = int(input("Year: "))
m2 = int(input("Month: "))
d2 = int(input("Day: "))

# second, create the date objects from the user input

first_date = datetime.date(y1, m1, d1)
second_date = datetime.date(y2, m2, d2)

# third, calculate the days between those dates and print it out in a formatted string

delta = abs(second_date - first_date)

print(f"There are {delta.days} days between those dates.")
