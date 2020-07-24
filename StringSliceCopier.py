# this exercise asks me to copy the first two characters of a string a number of times.

given_string = input("Enter string here: ")


def string_slice_copier(string):
    multiplier = int(input("Copies: "))
    if len(string) >= 2:
        return string[:2] * multiplier
    else:
        return string * multiplier


print(string_slice_copier(given_string))
