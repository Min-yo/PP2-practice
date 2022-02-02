n = int(input())
list = [1]
for x in range(0, n):
    list.append(str(input()))
for x in range(1, n+1):
    if list[x].rfind("@gmail.com") != -1:
        for c in list[x]:
            if c == '@':
                break
            print(c, end='')
        print(end='\n')