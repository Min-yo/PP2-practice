n = int(input())
s = [int(x) for x in input().split()] #x, y = [int(x) for x in input().split()] 
max0 = max1 = int(0)
for x in s:
    if x >= max1:
        max0 = max1
        max1 = x
    if x > max0 and x < max1:
        max0 = x

print(max1*max0)