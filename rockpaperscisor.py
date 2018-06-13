def playrockpaperscissor():
    print("*************Welcome to game of rock paper scissors **************** \n\n Choose your options wisely Rock Paper Scissors \n"
                     " Enter R for ROCK \n "
                     "Enter S for Scissors \n "
                     "Enter P for Paper\n"
                     "******************************************************************** \n")
    player1 = input("Player ONE choose your option:- ")
    player2 = input("Player TWO choose your option:- ")

# ROCK
    if player1 == "r" and player2 == "p":
        print ("Drum Rollsssssss Player 2 wins")
    if player1 == "r" and player2 == "s":
        print ("Drum Rollsssssss Player 1 wins")

# Paper
    if player1 == "p" and player2 == "s":
        print ("Drum Rollsssssss Player 2 wins")
    if player1 == "p" and player2 == "2":
        print ("Drum Rollsssssss Player 1 wins")

# ROCK
    if player1 == "s" and player2 == "r":
        print ("Drum Rollsssssss Player 2 wins")
    if player1 == "s" and player2 == "p":
        print ("Drum Rollsssssss Player 1 wins")


playrockpaperscissor()
playagain = input("Do you want to play again?????  y/n")
if (playagain == "y"):
    playrockpaperscissor()