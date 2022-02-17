def histogram(li):
    for x in li:
        for i in range(x):
            print("*", end="")
        print()
li = list(map(int, input().split()))
histogram(li)