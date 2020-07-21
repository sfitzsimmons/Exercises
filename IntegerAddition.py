# this exercise asks for me to take an integer (n) and compute the value of n+nn+nnn

# I'm going to go ahead and use a function to spice it up a tad

def int_addition(given_integer):
    n = int(given_integer)
    n1 = n
    n2 = int(f"{n}{n}")
    n3 = int(f"{n}{n}{n}")
    return n1 + n2 + n3


print(int_addition(input("Please enter an integer: ")))
