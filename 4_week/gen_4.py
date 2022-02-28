def squares(a, b) :
    for i in range(a, b):
        yield i*i
for i in squares(3, 8):
    print(i)