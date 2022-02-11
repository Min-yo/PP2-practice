import math 
x0, y0 = [int(x) for x in input().split()]
n = int(input())
di = dict()
li = li1 = []
for x in range(n):
    x, y = [int(x) for x in input().split()]
    distance = math.sqrt((x-x0)**2 + (y-y0)**2)
    point = str(x) + " " + str(y)
    if distance in di:
        li1.append(str(distance))
        li1.append(point)
        li.append(li1)
        li1 = []
    else: di[distance] = point
for x in sorted(di):
    for y in range(len(li)):
        if str(x) == (li[y][0]):
            print(li[y][1])
    print(di[x])