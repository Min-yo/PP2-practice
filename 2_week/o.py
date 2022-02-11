def Str_calc(s1, s2):
    temp = ""
    i1 = i2 = int(0)
    base = int(1)
    for x in range(len(s1)-1, -1, -1):
        temp += s1[x]
        if len(temp) > 2:
            if temp[::-1] == "ONE":
                i1 += 1*base
                base *= 10
            elif temp[::-1] == "TWO":
                i1 += 2*base
                base *= 10
            elif temp[::-1] == "THR":
                i1 += 3*base
                base *= 10
            elif temp[::-1] == "FOU":
                i1 += 4*base
                base *= 10
            elif temp[::-1] == "FIV":
                i1 += 5*base
                base *= 10
            elif temp[::-1] == "SIX":
                i1 += 6*base
                base *= 10
            elif temp[::-1] == "SEV":
                i1 += 7*base
                base *= 10
            elif temp[::-1] == "EIG":
                i1 += 8*base
                base *= 10    
            elif temp[::-1] == "NIN":
                i1 += 9*base
                base *= 10
            elif temp[::-1] == "ZER":
                base *= 10
            temp = ""
    base = int(1)
    temp = ""
    for x in range(len(s2)-1, -1, -1):
        temp += s2[x]
        if len(temp) > 2:
            if temp[::-1] == "ONE":
                i2 += 1*base
                base *= 10
            elif temp[::-1] == "TWO":
                i2 += 2*base
                base *= 10
            elif temp[::-1] == "THR":
                i2 += 3*base
                base *= 10
            elif temp[::-1] == "FOU":
                i2 += 4*base
                base *= 10
            elif temp[::-1] == "FIV":
                i2 += 5*base
                base *= 10
            elif temp[::-1] == "SIX":
                i2 += 6*base
                base *= 10
            elif temp[::-1] == "SEV":
                i2 += 7*base
                base *= 10
            elif temp[::-1] == "EIG":
                i2 += 8*base
                base *= 10    
            elif temp[::-1] == "NIN":
                i2 += 9*base
                base *= 10
            elif temp[::-1] == "ZER":
                base *= 10
            temp = ""
    return i1 + i2



s = input()
for x in range(len(s)):
    if s[x] == "+":
        s1 = s[:x]
        s2 = s[x+1:]
        break
sum = str(Str_calc(s1, s2))
ans = ""
for x in sum:
    if x == '1':
        ans += "ONE"
    elif x == "2":
        ans += "TWO"
    elif x == "3":
        ans += "THR"
    elif x == "4":
        ans += "FOU"
    elif x == "5":
        ans += "FIV"
    elif x == "6":
        ans += "SIX"
    elif x == "7":
        ans += "SEV"
    elif x == "8":
        ans += "EIG"
    elif x == "9":
        ans += "NIN"
    elif x == "0":
        ans += "ZER"
print(ans)

