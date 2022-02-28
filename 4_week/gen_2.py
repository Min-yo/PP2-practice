class gener:
    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < self.n:
            cur = self.num
            self.num += 2
            return cur
        raise StopIteration()


for x in gener(int(input())):
    print(x, end=", ")