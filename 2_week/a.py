ar = [int(x) for x in input().split()]
def recur(ar):
    if (ar[0]+1 >= len(ar)) or (len(ar) == 1):
        return True
    elif ar[ar[0]] == 0:
        for j in range(1, ar[0]+1):
            if ar[j] == 0:
                continue
            else: return recur(ar[j:])
        return False
    else: 
        for j in range(ar[0], 0, -1):
            if j < len(ar) and ar[j] > 0:
                if recur(ar[j:]):
                    return True
        return False

if recur(ar):
    print(1)
else: print(0)

#Time-limit exceeded - 73 test