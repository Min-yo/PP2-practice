lu = [int(x) for x in input().split()]
if len(lu) < 2:
    n = lu[0]
    x = int(input())
else: 
    n = lu[0]
    x = lu[1]
    

l = list()
for i in range(n):
    l.append(x + 2*i) 
ans = l[0]
for i in range(1, n):
    ans = ans^int(l[i])
print(ans)