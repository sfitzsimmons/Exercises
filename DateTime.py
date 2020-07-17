# This exercise uses the datetime module to display the current date and time

# first, import the datetime module
import datetime

# create a datetime object for right now
now = datetime.datetime.now()

print("Current date and time : ")
# print out the current year, month, day, hours, minutes, and seconds. Format it how I want it or I get milliseconds
print(now.strftime("%Y-%m-%d %H:%M:%S"))

