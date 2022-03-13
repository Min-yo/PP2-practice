import os
for x in range(ord('A'), ord('Z')+1):
    if not os.path.exists('.\\' + str(chr(x)) + '.txt'):
        f = open(chr(x)+'.txt', "x")
