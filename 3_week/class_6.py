class Prime:
    def __init__(self, liste = [0]):
        self.liste = liste
    def filter(self):
        ans = []
        for x in self.liste:
            flag = True
            for i in range(2, x):
                t = lambda y : True if (y % i == 0) else None
                if t(x):
                    flag = False
            if flag:
                ans.append(x)
        print(ans)

p1 = Prime([3, 2 , 5, 10, 11, 14, 13, 56])
p1.filter()


"""
flag = True
for x in range(2, distance):
    if(distance % x == 0):
        flag = False
"""