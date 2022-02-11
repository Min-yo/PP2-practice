brackets = input()
li = []
bo = True
for x in brackets:
    if x == '(' or x == '{' or x == '[':
        li.append(x)
    else: #x =='}' or x == ')' or x == ']'
        if len(li) == 0:
            bo = False
            break
        elif x == ')' and li[-1] != '(':
            bo = False
            break
        elif x == ']' and li[-1] != '[':
            bo = False
            break
        elif x == '}' and li[-1] != '{':
            bo = False
            break
        li.pop(-1)
if len(li) == 0:
    print("Yes")
else: print("No")
    
#if x =='}' or x == ')' or x == ']':
    
    