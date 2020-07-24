# this exercise wants me to take a string and return it copied n number of times.


def string_copier(string):
    start = string
    copies = int(input("How many times do you want this string copied? "))
    end = start * copies
    return end


print(string_copier(input("Enter string: ")))
