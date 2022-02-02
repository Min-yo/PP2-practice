n = int(input())
list = [1]
for x in range(0, n):
    list.append(int(input()))
for x in range(1, n+1):
    if list[x] <= 10:
        print("Go to work!")
    elif list[x] > 10 and list[x] <=25:
        print("You are weak")
    elif list[x] > 25 and list[x] <=45:
        print("Okay, fine")
    else:
        print("Burn! Burn! Burn Young!")