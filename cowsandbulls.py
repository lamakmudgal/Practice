import random
digitlist = random.randrange(999,9999)
print(digitlist)

listofnumber = [char for char in str(digitlist)]
print(listofnumber)
userinput = input("Please enter 4 digit numbers:- ")
userguess = [char for char in str(userinput)]

cow =0
bull = 0
correct = False
while correct == False:
    for i in range(0,4):
        for userguessdigit in userguess:
            if (userguessdigit == listofnumber[i]):
                cow = cow+1
            else:
                bull=bull+1
    if cow == 4:
        print("correct guess")
        cow = 0
        bull = 0
        correct = True
    else:
        print("You have %s cows and %s bulls",cow,bull)
        cow = 0
        bull = 0
        userinput = input("Please Guess again:- ")
        userguess = [char for char in str(userinput)]







