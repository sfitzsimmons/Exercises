# this exercise asks me to determine if a Python shell is executing in a 32bit or 64bit mode on OS.

import struct

print(struct.calcsize("P") * 8)
