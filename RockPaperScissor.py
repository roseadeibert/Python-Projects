import random

name = input("Hello! What is your name? ").lower
print("Would you like to play Rock, Paper, Scissors?")

answer = input("Yes or No? ")

if answer == "yes".lower():
    print("Let's get started!")
elif answer == "no".lower():
    print("That's okay come back when you do :).")
    exit()
else:
    print("Maybe next time! See ya later.")

while answer != "no": 

    print("rock (1), paper(2),(scissors(3)")
    print('')

    rock = 1
    paper = 2
    scissors = 3

    player = int(input("Enter choice. "))

    computer = random.randint(1,3)

    if player == 1:
        print("Rock!")
    elif player == 2:
        print("Paper!")
    elif player == 3:
        print("Scissors!")
    else:
        print("Invalid answer.")


    if computer == 1:
        print("Computer chose rock.")
    elif computer == 2:
        print("Computer chose paper.")
    elif computer == 3:
        print("Computer chose scissors.")
    else:
        print("Invalid answer.")




    if player == 1 and computer == 1:
        print("It's a tie.")
    elif player == 1 and computer == 3:
        print("You win :)")
    elif player == 1 and computer == 2:
        print("You lose :(")
    elif player == 2 and computer == 2:
        print("It's a tie!")
    elif player == 2 and computer == 1:
        print("You win :)")
    elif player == 2 and computer == 3:
        print("You lose :(")
    elif player == 3 and computer == 3:
        print("It's a tie!")
    elif player == 3 and computer == 2:
        print("You win :)")
    elif player == 3 and computer == 1:
        print("You Lose :(")
        
    answer = input("Do you want to play again? ")

    if answer == "no".lower():
        print("That's okay come back when you do :).")
    