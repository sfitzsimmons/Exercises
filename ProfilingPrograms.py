# this exercise asks for me to determine profiling of Python programs

import cProfile

data = [[1, 2, 3], ["a", "b", "c"], ["x", "y", "z"], [9, 8, 7]]


def funk(l1):
    for i in l1:
        for k in i:
            print(k, i)


funk(data)
cProfile.run('funk(data)')
