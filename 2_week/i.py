n = int(input())
li = []
ans = []
for x in range(n):
    k = [str(i) for i in input().split()]
    if k[0] == '2' and len(li) == 0:
        continue
    elif k[0] == '1':
        li.append(k[1])
        
    elif k[0] == '2': 
        ans.append(li[0])
        li.pop(0)
        
for x in ans:
    print(x, end=" ")

