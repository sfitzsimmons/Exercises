# this exercise asks me to take all the elements in a list and concentrate them into a string.

starting_list = ["Here", "is", "my", "list", "full", "of", "words", "to", "concentrate", "into", "a", "string"]

final_string = ""

for element in starting_list:
    final_string = final_string + element + " "

print(final_string)


# as a function:
print("\nAs a function:\n")


def list_concentrator(list):
    product = ""
    for element in list:
        product = product + element + " "
    return product


print(list_concentrator(starting_list))

