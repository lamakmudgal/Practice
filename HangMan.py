import random
#listofwords = []
def readDictionary():
    with open('sowpods.txt','r') as dictofwords:
        return(dictofwords.readlines())




def choosewordfromlistofwords(listofwordparameter):
    #wordint = random.randint(0,len(listofwordparameter))
    #print(wordint)
    chosenword =  listofwordparameter[random.randint(0,len(listofwordparameter))].rstrip("\n")
    print("The randomly selected word is:- ", chosenword)
    return chosenword

def analyzeuserinput(guessfromuser, selectawordfromdict):
    listofselectawordfromdict = list(selectawordfromdict)
    listofguess = ["_" for i in range(0,len(listofselectawordfromdict))]
    correctguesscount = 1
    while (correctguesscount < len(listofselectawordfromdict)-1):
        if (guessfromuser not in selectawordfromdict):
            print("------ sorry letter not in the word --------")
        elif (guessfromuser in listofselectawordfromdict):
            correctguesscount = correctguesscount +1
            print("correctguesscount", correctguesscount)
            for i in range(0,len(listofselectawordfromdict)):
                if (listofselectawordfromdict[i]==guessfromuser):
                    listofguess[i] = guessfromuser
        print(listofguess)
        guessfromuser = input("Please guess your next letter:-")
    print("Congratulation you won")
def printHang(n):
    gal = [['---- '],
           ['|  | '],
           ['|    '],
           ['|    '],
           ['|    ']]
    if n < 6:
        gal[2] = ['|  o ']
    if n < 5:
        gal[3] = ['| /  ']
    if n < 4:
        gal[3] = ['| / \\']
    if n < 3:
        gal[3] = ['| /|\\']
    if n < 2:
        gal[4] = ['| /  ']
    if n < 1:
        gal[4] = ['| / \\']
    for i in gal:
        print(''.join(i))

listofwords  = readDictionary()

printHang(0)
selectawordfromdict = choosewordfromlistofwords(listofwords)
guessfromuser = input("Please guess your letter:-")
analyzeuserinput(guessfromuser, selectawordfromdict)







