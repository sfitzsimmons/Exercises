# this exercise asks for me to check to see if a file exists

import os.path

open('abc.txt', 'w')
print(os.path.isfile('abc.txt'))

