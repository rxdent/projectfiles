import random
import os

options = ["rock", "paper", "scissors"]
uscore = []
rscore = []

def name():
    os.system("clear")
    n = input("Please enter your name: ").capitalize()
    return n

def robot():
    rchoice = random.choice(options)
    return rchoice


def game():
    choice = "a"
    while choice not in options:
        os.system("clear")
            
        choice = input("Rock, paper, or scissors?: ").lower()

        if choice not in options:
            os.system("clear")
            input("Please type rock, paper, or scissors only. Press enter to continue...")
    return choice

def compare(rob,usr):
    os.system("clear")

    if (usr == "paper" and rob == "rock") or (usr == "scissors" and rob == "paper") or (usr == "rock" and rob == "scissors"):
        print("You won!")
        result = "won"
    elif usr == rob:
        input(f"You both picked {usr}! Go again! Press enter to continue...")
        result = "same"
    else:
        print("You lost!")
        result = "lost"
    return result
        
def score(r):
    print()
    if r == "won":
        uscore.append(1)
        print(f"1 point was added to your score! Your score is now: {sum(uscore)}")
    else:
        rscore.append(1)
        print(f"1 point was added to the robot's score! Robot's score is now: {sum(rscore)}")




def program():
    play = True
    os.system("clear")
    input(f"Rock paper scissors! Rock beats scissors, scissors beats paper, and paper beats rock. Press enter to continue...")
    n = name()
    while play:
        rchoice = robot()
        choice = game()
        print(f"\nRobot chose: {rchoice}")
        print(f"\nYou chose: {choice}")
        input("\nPress enter to continue...")
        result = compare(rchoice, choice)
        if result != "same":
            score(result)
            print(f"\n{n}'s score: {sum(uscore)}")
            print(f"\nRobot's score: {sum(rscore)}")
            play = input("\nPlay again? Type y for anything else for no: ")
        
            if play == "y":
                continue

            else:
                os.system("clear")
                print(f"Final score:\n User: {sum(uscore)}\n Robot: {sum(rscore)}\n")
                print("Program ended.")
                play = False


program()