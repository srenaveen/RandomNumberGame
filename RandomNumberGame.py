import random

guess=input("ENTER GUESS HERE: ")
chances=0
number=random.randrange(1,10)
while chances < 5:
    if(guess==number):
        print("Great job! Correct answer!")
        chances=5
    elif(guess<number):
        print("Answer is greater")
    elif(guess>number):
        print("Answer is lesser")
if not chances==5:
    print("Game Over!")