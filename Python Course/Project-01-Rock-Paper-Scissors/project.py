"""
1 for Rock
2 for Paper
3 for Scissor

Rock vs Paper -> Paper Wins | Paper vs Scissors -> Scissors Wins | Scissors vs Rock -> Rock Wins
"""

import random

yesNo = input("Do you want to play Rock, Paper, Scissor ? (Yes/No) : ")

while(yesNo.capitalize() == 'Yes'):

    gameRules = {1: "Rock", 2: "Paper", 3: "Scissor"}

    userSelection = {"Rock": 1, "Paper": 2, "Scissor": 3}

    yourInput = input("Rock, Paper, Scissor, Shoot : ")

    your_choice = userSelection[yourInput.capitalize()]
    cpu_choice = random.choice([1, 2, 3])

    print(f"You chose {yourInput} and Cpu chose {gameRules[cpu_choice]}")

    if(your_choice == 1 and cpu_choice == 1):
        print("Draw")
    elif(your_choice == 2 and cpu_choice == 2):
        print("Draw")
    elif(your_choice ==3 and cpu_choice == 3):
        print("Draw")
    else:
        if(your_choice == 1 and cpu_choice == 2):
            print("Cpu Wins")
        elif(your_choice == 1 and cpu_choice == 3):
            print("You Wins")
        elif(your_choice == 2 and cpu_choice == 1):
            print("You Wins")
        elif(your_choice == 2 and cpu_choice == 3):
            print("Cpu Wins")
        elif(your_choice == 3 and cpu_choice == 1):
            print("Cpu Wins")
        elif(your_choice == 3 and cpu_choice == 2):
            print("You Wins")
        else:
            print("Invalid Command")

    if(yesNo.capitalize() == 'No'):
        break