from time import sleep
import math
numb = int(input())
milisec = int(input())
sleep(milisec/1000)
print("Square root of " + str(numb) + " after " + str(milisec) + " miliseconds is "+ str(math.sqrt(numb))) 