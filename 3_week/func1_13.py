from random import randint

def guess_random():
    print("Hello! What is your name?")
    name = input()
    b = randint(1, 20)
    print("Well, "+ name +", I am thinking of a number between 1 and 20.")
    print('Take a guess.')
    a = int(input())
    cnt = 0
    while True:
        cnt += 1
        if a == b:
            print('Good job, ' + name + '! You guessed my number in '+ str(cnt) +' guesses!')
            return
        elif a < b:
            print('Your guess is too low.')
            print('Take a guess.')
            a = int(input())
            print()
        elif a > b:
            print('Your guess is too high.')
            print('Take a guess.')
            a = int(input())
            print()
guess_random()
