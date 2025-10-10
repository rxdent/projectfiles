# The point of the game is to see who gets closer to 20.
# User will have a total amount of coins to start with.
# User will select how many coins are going to be in play (cannot exceed total remaining amount).
# Each player (human and computer) will draw ONCE from 1 to 10, and then wait for their turn to play again.
# Example: user gets 8, and then the computer gets 6. User get 7, (will show a total of 15), and then the
# computer will get 10 (will show a total of 16). If the computer total is equal to or greater than 16, the computer will not draw more numbers.

import random
import os


#Variables/Lists/etc---------------

starting_amount = random.randint(1, 20)
user_coins = [starting_amount] #How many coins the user has
pcoinsadded = 0 #How many coins the user WANTS to put in play
coins_in_play = [] #coins in play
user_wins = 0 
comp_wins = 0

#Colors ----------------------------

GREEN =  "\033[32m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
BOLD = "\033[1m"
RESET = "\033[0m"
RED = "\033[31m"

#Code -----------------------------

os.system("clear")

user = input("Please enter your name: ")

os.system("clear")

start = input(f"""Welcome to the game: {MAGENTA}{BOLD}Twenty!{RESET} The goal of the game is to {MAGENTA}draw numbers{RESET} till you get closer to {GREEN}20{RESET}, without exceeding {GREEN}20{RESET}. 
Type {MAGENTA}y{RESET} to begin playing {MAGENTA}or anything else{RESET} to exit the game!: """).lower()

while start == "y":

    os.system("clear")
    pcoins = "y"

    input(f"""You currently have {GREEN}{sum(user_coins)}{RESET} coins. You put them in play to {MAGENTA}DOUBLE{RESET} the amount every time you win. Every time you lose, the computer takes your coins.
Note: You cannot put coins in play more than you own. {MAGENTA}Press enter to continue...{RESET}""")

    while pcoins == "y":
        os.system("clear")
        print(f"Coins: {GREEN}{sum(user_coins)}{RESET}\n")
        pcoinsadded = input("How many coins do you want to put in play?: ")

        try:
            if int(pcoinsadded) <= sum(user_coins):
                coins_in_play.append(pcoinsadded)
                pcoins = "a"
            else:
                os.system("clear")
                input(f"That is not a valid answer. Type numbers only and don't exceed the amount of coins you currently own. {MAGENTA}Press enter to continue...{RESET}")       

        except:
            os.system("clear")
            input(f"That is not a valid answer. Type numbers only and don't exceed the amount of coins you currently own. {MAGENTA}Press enter to continue...{RESET}")


    user_amount = [] #how many numbers the user has drawn
    comp_amount = [] #how many numbers the computer has drawn
    user_sum = 0 #The sum of the user amount
    comp_sum = 0 #The sum of the comp amount

    while user_sum < 20 and comp_sum < 20:

        os.system("clear")

        while True:

            os.system("clear")

            print(f"{CYAN}{user.capitalize()}'s Amount:{RESET} {GREEN}{user_sum}{RESET}\n")
            print(f"{RED}Computer's Amount:{RESET} {GREEN}{comp_sum}{RESET}\n")
            draw = input(f"{MAGENTA}Press y{RESET} to draw a number. Press {MAGENTA}n to not draw one...:{RESET} ").lower()

            if draw == "y":

                user_amount.append(random.randint(1,10))
                print(f"\nYou drew {GREEN}{user_amount[-1]}{RESET}")
                user_sum = sum(user_amount)
                input(f"\nNew Amount: {GREEN}{user_sum}{RESET}")
                break

            elif draw == "n":
                break

            else:
                os.system("clear")
                input("Please type {MAGENTA}Y or N only.{RESET} Press enter to continue...")

        if user_sum > 20:
            break

        os.system("clear")

        if comp_sum > 20:
            break

        if comp_sum >= 16:
            cont = input(f"{RED}Computer{RESET} has reached {GREEN}16{RESET} and will no longer draw numbers. Do you want to continue to draw cards to see if you can get a higher number? {MAGENTA}Type y for yes and anything else for no:{RESET} ").lower()
            if cont == "y":
                continue
            else:
                break

        elif comp_sum <= 16:
            comp_amount.append(random.randint(1,10))
            comp_sum = sum(comp_amount)
            print(f"{RED}Computer{RESET} drew a {GREEN}{comp_amount[-1]}{RESET}")
            print(f"\n{CYAN}{user.capitalize()}'s{RESET} Amount: {GREEN}{user_sum}{RESET}")
            input(f"\n{RED}Computer's{RESET} Amount: {GREEN}{comp_sum}{RESET}")
            cont = "y"

    if user_sum >= 20:
        os.system("clear")
        total_coins = sum(user_coins)
        user_coins.clear()
        user_coins.append(total_coins - int(pcoinsadded))

        input(f"You lost... {RED}Computer{RESET} took {GREEN}{pcoinsadded}{RESET} of your coins! You have {GREEN}{sum(user_coins)}{RESET} coins remaining. {MAGENTA}Press enter to continue...{RESET}")
        comp_wins += 1

    elif comp_sum >= 20:
        os.system("clear")
        user_coins.append(int(pcoinsadded) * 2)
        total_coins = sum(user_coins)
        user_coins = [total_coins]
        input(f"You won!!! Your coins in play DOUBLED! You now have {GREEN}{total_coins}{RESET} coins! {MAGENTA}Press enter to continue...{RESET}")
        user_wins += 1

    else:
        if user_sum > comp_sum:
            os.system("clear")
            user_coins.append(int(pcoinsadded) * 2)
            total_coins = sum(user_coins)
            user_coins = [total_coins]
            input(f"You won!!! Your coins in play DOUBLED! You now have {GREEN}{total_coins}{RESET} coins! {MAGENTA}Press enter to continue...{RESET}")
            user_wins += 1
        
        elif comp_sum > user_sum:
            os.system("clear")
            total_coins = sum(user_coins)
            user_coins.clear()
            user_coins.append(total_coins - int(pcoinsadded))
            input(f"You lost... {RED}Computer{RESET} took {GREEN}{pcoinsadded}{RESET} of your coins! You have {GREEN}{sum(user_coins)}{RESET} coins remaining. {MAGENTA}Press enter to continue...{RESET}")
            comp_wins += 1
        
        else:
            os.system("clear")
            input(f"It's a tie! Neither of you get coins! {MAGENTA}Press enter to continue...{RESET}")
        
    if sum(user_coins) <= 0:
        os.system("clear")
        input(f"You are out of coins... {RED}GAME OVER.{RESET} {MAGENTA}Press enter to continue...{RESET}")
        break
    
    else:
        os.system("clear")
        print(f"{CYAN}{user.capitalize()}{RESET} wins: {user_wins}\n")
        print(f"{RED}Computer{RESET} wins: {comp_wins}\n")
        start = input(f"Do you want to keep playing? {MAGENTA}Type y for yes and anything else for no:{RESET} ").lower()


os.system("clear")

print(f"Thank you for playing {MAGENTA}Twenty!{RESET} We hope to see you again soon!")