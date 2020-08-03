# this exercise asks for me to add two objects if they're both integer types.


def int_adder(x, y):
    if type(x) == int and type(y) == int:
        return x + y
    else:
        raise TypeError("Inputs must be integers")


object1 = 6
object2 = 90

print(int_adder(object1, object2))
