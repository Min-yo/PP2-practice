s = input()
def reverse_str(s):
    s1 = [str(x) for x in s.split()]
    for x in reversed(s1):
        print(x, end=" ")
reverse_str(s)