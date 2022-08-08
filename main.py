""" The Winning Rules are as follows:

Rock smashes Scissors.
Paper covers Rock.
Scissors cut Paper.

Enter a choice (Rock(r), Paper(p), Scissors(s)): r
    
You chose Rock, the computer chose Paper.

Paper covers Rock! You lose.

Play again? (y/n): y
Enter a choice (Rock(r), Paper(p), Scissors(s)): p

You chose Paper, computer chose Paper.

Both players selected Paper. It's a tie!

Play again? (y/n): n
Final Scores:
Computer: 1
Player: 0 """

import random

################### FUNCTIONS #############################

#create function to rename choices

def getFullName(x):
    if x == "r":
        x = "Rock"
    elif x == "p":
        x = "Paper"
    elif x == "s":
        x = "Scissors"
    return x

#create a function to validate options

def validateChoice(x):
    if x =="r" or x== "p" or x=="s":
        return True
    else:
        return False

##################################  MAIN #########################
user_score = 0
pc_score = 0

while True:

    #Ask user for a choice
    user = input("Enter a choice (Rock(r), Paper(p), Scissors(s))")
    if validateChoice(user) == False:
        print("Invalid choice")
        continue
    #Convert choice to full name
    user = getFullName(user)
    print ("Your choice:", user)
    #Generate random choice r, p or s
    computer = random.choice("rps")
    
    #Convert computer random letter to full name
    computer = getFullName(computer)
    
    print ("Computer's choice:", computer)
    #Check for draw
    if user == computer:
        print("Both players selected", user,"It's a tie!")
    #Check for winning
    elif user == "Rock" and computer == "Scissors":
        print("Rock smashes Scissors! You win.")
        user_score+=1
    elif user == "Paper" and computer == "Rock":
        print("Paper covers rock. You win")
        user_score+=1
    elif user == "Scissors" and computer == "Paper":
        print("Scissors cut paper. You win")
        user_score+=1
    #Check for lossing
    elif computer == "Rock" and user == "Scissors":
        print("Rock smashes Scissors! You lose.")
        pc_score+=1
    elif computer == "Paper" and user == "Rock":
        print("Paper covers rock. You lose")
        pc_score+=1
    elif computer == "Scissors" and user == "Paper":
        print("Scissors cut paper. You lose")
        pc_score+=1

    print("Final scores\nComputer:", pc_score, "\nPlayer:", user_score)

    while True:
        play_again = input("Play again? y/n").lower()
        if play_again == "y":
            break
        elif play_again == "n":
            quit()
        else:
            print("Invalid option")
            continue