import random
import sys

low = int(sys.argv[1])
hi = int(sys.argv[2])

secret_num = random.randint(low, hi)
while True:
    try:
        guess = int(input("what is your guess? "))
        if guess == secret_num:
            print("You're right!")
            break
        else:
            print("try again")
    except ValueError:
        print("please enter a number")
        continue
