class gener:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= 0:
            cur = self.n
            self.n -= 1
            return cur
        raise StopIteration()

for x in gener(10):
    print(x, end= ", ")