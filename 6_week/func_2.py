st = input()
cntUp = cntLow =0
for x in st:
    if ord(x) >= ord('A') and ord(x) <= ord('Z'):
        cntUp += 1
    elif ord(x) >= ord('a') and ord(x) <= ord('z'):
        cntLow += 1
print('Upper: ' + str(cntUp) + ' Lower: ' + str(cntLow))