import os
with open(r".\Test\test.txt") as path:
    x = len(path.readlines())
print(x)