li = [int(x) for x in input().split()]
def sort_primes(list):
    ans = []
    for i in list:
        flag = True
        for x in range(2, i):
            if(i % x == 0):
                flag = False
                break
        if flag and i != 1:
            ans.append(i)
    return ans
print(sort_primes(li))