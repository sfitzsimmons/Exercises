# this exercise asks for me to list all files in a directory

from os import listdir
from os.path import isfile, join

files_list = [f for f in listdir('/Users/plumb/PycharmProjects/exercises')
              if isfile(join('/Users/plumb/PycharmProjects/exercises', f))]
print(files_list)

