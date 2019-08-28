def printboard():
    a = '---'.join('    ')
    b = '   '.join('||||')
    print('\n'.join((a, b, a, b, a, b, a)))
row1 = [5,5,5]
row2 = [5,5,5]
row3 = [5,5,5]
finalresult = [row1,
               row2,
               row3]

def checkResult(finalresult):
    if(finalresult[0][0]==finalresult[0][1]==finalresult[0][2] or
            finalresult[0][0]==finalresult[1][0]==finalresult[2][0] or
            finalresult[0][0]==finalresult[1][1]==finalresult[2][2] ):
        print("Payer 2 win")
    elif (finalresult[0][1]==finalresult[1][1]==finalresult[2][1]):
        print("Payer 1 win")
    elif(finalresult[0][2]==finalresult[1][1]==finalresult[2][0] or
            finalresult[0][2]==finalresult[1][2]==finalresult[2][2] ):
        print("Payer 3 win")
    elif(finalresult[1][0]==finalresult[1][1]==finalresult[1][2] or
                finalresult[2][0]==finalresult[2][1]==finalresult[2][2] ):
        print("Row Match")

def userinput():
     print("--------Welcome to the game of Tic Tac Toe------")
     printboard()
     print("Please enter your input as Row,Column,1 or 2. Player 1 is 1 and Player 2 is 2")
     count = 9
     while(count):
         player1input = input("Player Please make your move:-")
         finalresult[int(player1input[0])-1][int(player1input[1])-1] = int(player1input[2])
         print(finalresult[0],"\n",finalresult[1],"\n",finalresult[2])
         count = count-1



printboard()
#checkResult(finalresult)
userinput()
checkResult(finalresult)