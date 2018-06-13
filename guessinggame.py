import random

randomnumber = random.randint(0,9)

userinput = int(input("I have a number between 0- 9. Can you guess it??? :- "))
correct = False
while(correct == False):
    if randomnumber == userinput:
        correct = True
        print("Congratulation")

    if randomnumber > userinput:
        userinput = int(input("Please guess higher:- "))
    elif randomnumber < userinput:
        userinput = int(input("Please guess lower:- "))

