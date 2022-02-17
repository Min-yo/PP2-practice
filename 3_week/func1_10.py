li = list(map(int,input().split()))
def unique(li):
    ans = []
    for x in range(len(li)):
        flag = True
        for y in li[x+1:]:
            if li[x] == y:
                flag = False
                break
        if flag:
            ans.append(li[x])
    return ans
print(unique(li))