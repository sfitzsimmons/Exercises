# this exercise asks for a user filename as an input and then prints the file's extension.

filename = input("Enter the filename: ")

# I only want the extension of the filename, so I have to split the filename at the "."
file_extension = filename.split(".")

# I split the filename into two pieces, but I only want the last piece.
# I use the repr() function and specify that I want the last piece. The [-1] piece.
print("The extension of the file is: " + repr(file_extension[-1]))
