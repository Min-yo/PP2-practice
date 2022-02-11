n= int(input())
di = dict()
s, numb = [str(x) for x in input().split()]
di[s] = int(numb)
for x in range(1, n):
    g, j = [str(x) for x in input().split()]
    j = int(j)
    if g in di:
        di[g] += j
    else: di[g] = j
max = int(0)
for x in di:
    if di[x] > max:
        max = di[x]

for x in sorted(di):
    if di[x] == max:
        print(str(x) + " is lucky!")
    else: print(str(x) + " has to receive " + str(max - di[x]) + " tenge")

