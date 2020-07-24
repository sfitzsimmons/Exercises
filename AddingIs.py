# this exercise wants me to take a string and add "Is" to the beginning of it unless the string already starts
# with "Is".

given_string = input("Enter your string: ")

if given_string[:2] == "Is":
    print(given_string)
else:
    print(f"Is {given_string}")
