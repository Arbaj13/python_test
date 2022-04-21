from ast import While
from queue import PriorityQueue
import random

from scipy import rand

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input(f"guess the number between 1 and {x}: "))
        if random_number>guess:
            print("it too low")
        elif random_number<guess:
            print("it too high")

    print(f"you have guess correct nuber {random_number}")

def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low #could be high as here high=low
        feedback=input(f"the computer has guessed number {guess} !! .... is it  Too High (H) ,Too low (L) or correct(C) ??:").lower()
    
        if feedback=='h':
                high=guess-1
        elif feedback=='l':
                low=guess+1
              
        


    print(f"yes computer has guess is correctly {guess}")




x=int(input("Please enter a range  number: "))
computer_guess(x)          









