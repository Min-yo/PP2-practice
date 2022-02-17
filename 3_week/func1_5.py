#all permutations
st = input()
from itertools import permutations
perm = permutations(st)
for x in list(perm):
    print (x)