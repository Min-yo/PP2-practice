n = int(input())
if n % 2 != 0:
    for x in range(n):
        for y in range(n):
            if x + y >= n-1:
                print("#", end="")
            else: print(".", end="")
        print()
else:
    for x in range(n):
        for y in range(n):
            if x == y:
                print("#", end="")
            elif x > y:
                print("#", end="")    
            else: print(".", end="")
        print()
    