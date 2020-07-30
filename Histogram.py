# this exercise asks for me to print a histogram from a list of values


def histogram(entries):
    print("        HISTOGRAM        ")
    print("_________________________")
    for value in entries:
        print_line = ""
        print_symbol = "@ "
        print(" |", (print_line + print_symbol)*value)
    print(" 0-1-2-3-4-5-6-7-8-9")
    print("_________________________")


histogram([2, 3, 6, 5, 9, 9, 2, 3, 5, 4,])
