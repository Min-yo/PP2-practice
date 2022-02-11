s = set([str(x) for x in input().split()])      
print(len(s))
for x in sorted(s):
    for y in x:
        if y.isalpha():
            print(y, end="")

    print()