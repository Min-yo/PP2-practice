li = []
while True:
    t = int(input())
    if t == 0:
        break
    li.append(t)
for x in range(int(len(li)/2)):
    print(li[x]+li[-(x+1)], end=" ")
if len(li) % 2 != 0:
    print(li[int(len(li)/2)])
    