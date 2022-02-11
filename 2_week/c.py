n = int(input())

for x in range(n):
    for y in range(n):
        if x == 0: print(y, end=" ")
        elif y == 0: print(x, end=" ")
        elif x == y: print(x*y, end=" ")
        elif x != y: print(0, end=" ")
    print()