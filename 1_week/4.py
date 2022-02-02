numb = int(input())
s = str(input())
if s == "k":
    c = int(input())
    ans = float(numb/1024)
    print(f"{ans:.{c}f}")
else:
    print(numb*1024)
