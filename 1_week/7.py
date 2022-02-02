s = str(input())
sum = int(0)
'''
base = 2**(len(s)-1)
for x in s: 
    sum = sum + int(x)*base
    base = base/2
print(int(sum))
'''
base = int(1)
for x in reversed(s):
    sum += int(x)*base
    base *= 2
print(sum)