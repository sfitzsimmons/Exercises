# this exercise asks me to write a program to count the number of times "4" appears in a given list.


def list_counter(l1):
    counter = 0
    for i in l1:
        if i == 4:
            counter += 1
    return counter


given_list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 33]
given_list2 = [2, 3, 4, 5, 4, 3, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 4, 3, 4, 5, 6, 5, 4, 0]

print(f"given_list1 has the number 4 in it {list_counter(given_list1)} times.")
print(f"given_list2 has the number 4 in it {list_counter(given_list2)} times.")



