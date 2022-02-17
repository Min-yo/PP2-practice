s = input()
def is_palindrom(s):
    if s[::-1] == s:
        return True
    else: return False
if is_palindrom(s):
    print("Yes")
else: print("No")