class gener:
    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num >= self.n: 
            raise StopIteration()
        elif self.num%3==0 and self.num%4==0:
                cur = self.num
                self.num += 1
                return cur
        self.num = self.num + 1


for x in filter(None, gener(100)):
    print(x, end=", ")