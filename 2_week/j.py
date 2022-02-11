n = int(input())
l = list()
for x in range(n):
    pas = input()
    if pas in l:
        continue
    else: l.append(pas)
l2 = list()
cnt = int(0)
for x in l:
    lower = upper = number = False
    for i in x:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            lower = True
        elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
            upper = True
        elif ord(i) >= ord('0') and ord(i) <= ord('9'):
            number = True
    if lower == True and upper == True and number == True:
        l2.append(x)
        cnt += 1
print(cnt)
for x in sorted(l2):
    print(x)
