# this exercise asks me to print all the even numbers from a given list that are less than 237 in the sequence.

# These instructions aren't written very clearly but I think this is what it's asking for.

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]

for num in numbers:
    if num == 237:
        print(num)
        break
    elif num % 2 == 0:
        print(num)




