t = 1
List_1 = []
while True:
    t = input()
    if t == '0':
        break
    t1 = [str(x) for x in t.split()]
    List_1.append(t1)
'''
for x in range(3):
    t = [int(x) for x in input().split()]
    List_1.append(t)
'''
for x in range(len(List_1)):
    for y in range(x+1, len(List_1)):
        if int((List_1[x])[2]) > int((List_1[y])[2]):
            temp = List_1[x]
            List_1[x] = List_1[y]
            List_1[y] = temp
        elif int((List_1[x])[2]) == int((List_1[y])[2]):
            if int((List_1[x])[1]) > int((List_1[y])[1]):
                temp = List_1[x]
                List_1[x] = List_1[y]
                List_1[y] = temp
            elif int((List_1[x])[1]) == int((List_1[y])[1]):
                if int((List_1[x])[0]) > int((List_1[y])[0]):
                    temp = List_1[x]
                    List_1[x] = List_1[y]
                    List_1[y] = temp

for x in List_1:
    for y in x:
        print(y, end=" ")
    print()

#Time-limit exceeded - 68 test