s = str(input())
t = str(input())
'''
if s.rfind(t) != -1:
    findLast = findFirst = s.rfind(t)
    while s.rfind(t, 0, findLast) != -1:
        findFirst = s.rfind(t, 0, findLast)
    if findLast != findFirst:
        print(findFirst + " " + findLast)
    else:
        print(findLast)
'''
cnt = int(-1)

if s.rfind(t) != -1:
    indexL = s.rfind(t)
    for x in s:
        cnt += 1
        if x == t and cnt != indexL:
            indexF = cnt
            break
        else:
            indexF = -1
    if indexF != -1 and indexL != indexF:
        print(str(indexF) + " " + str(indexL))
    else:
        print(indexL)


'''
for x in s:
    cnt1 += 1
    if x == t and cnt1 != indexL:
        indexF = cnt1
        break
'''

