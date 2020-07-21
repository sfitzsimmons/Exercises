# This exercise asks to print out the calendar of a given month/year using the calendar module

import calendar

year = int(input("Input the year: "))
month = int(input("Input the month: "))
print(calendar.month(year, month))
