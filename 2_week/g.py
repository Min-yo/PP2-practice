numb_demons = int(input())
di = dict()
di2 = dict()
name, weak = [str(x) for x in input().split()]
di[weak] = 1
for x in range(1, numb_demons):
    name, weak = [str(x) for x in input().split()]
    if weak in di:
        di[weak] += 1
    else: di[weak] = 1

numb_hunt = int(input())
name, abil, num = [str(x) for x in input().split()]
di2[abil] = int(num)
for x in range(1, numb_hunt):
    name, abil, num = [str(x) for x in input().split()]
    if abil in di2:
        di2[abil] += int(num)
    else: di2[abil] = int(num)
left = int(0)
#keysList = list(di.keys())
for x in list(di.keys()):
    if x in di2:
        if di[x]-di2[x] > 0:
            left += di[x]-di2[x]
    else: left += di[x]
print("Demons left: " + str(left))