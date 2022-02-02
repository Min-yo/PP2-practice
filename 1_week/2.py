sum = int(0)
for x in str(input()): #The function ord() gets the int value of the char.
    sum = sum + ord(x)
if sum > 300:
    print("It is tasty!")
else:
    print("Oh, no!")
