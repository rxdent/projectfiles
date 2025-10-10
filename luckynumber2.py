import random
import os

GREEN =  "\033[32m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
BOLD = "\033[1m"
RESET = "\033[0m"

numbers = list(range(1, 72))
play = "y"

def display():
    os.system("clear")
    print(f"Current numbers: {CYAN}{sorted(c_number_list)}{RESET}")
    c_number = input(f"Type in a number between {GREEN}1-70{RESET}. There are up to {GREEN}5{RESET} numbers: ")
    return c_number

def playing(x):
    try:
            c_number = int(x)

            if c_number in c_number_list:
                os.system("clear")
                input(f"You've already chosen that number! Pick a different number. Press enter to continue...")
                c_number_list.remove(c_number)

            if 0 < c_number <= 70:
                c_number_list.append(c_number)

            else: 
                os.system("clear")
                input(f"Type in a number between {GREEN}1-70{RESET} only. Press enter to continue...")
                
    except:
        os.system("clear")
        input(f"Type in a number between {GREEN}1-70{RESET} only. Press enter to continue...")

def sort(ln):
    os.system("clear")
    c_number_list.sort()
    global lucky_numbers
    lucky_numbers.sort()
    chosen_set = set(c_number_list)
    lucky_set = set(lucky_numbers)
    return chosen_set, lucky_set

def display2():
    print(f"Your numbers:\n{CYAN}{c_number_list}{RESET}\n")
    print(f"Your lucky numbers:\n{CYAN}{lucky_numbers}{RESET}\n")

def result(cs, ls):
    if c_number_list == lucky_numbers:
        print(f"WOW! You guessed {MAGENTA}all{RESET} the numbers! You get {GREEN}100{RESET} points!")

    elif len(cs.intersection(ls)) == 4:
        print(f"Yay! You got {MAGENTA}4/5{RESET} numbers correct! Your final score is {GREEN}30{RESET} points!")

    elif len(cs.intersection(ls)) == 3:
        print(f"Congrats! You got {MAGENTA}3/5{RESET} numbers correct! Your final score is {GREEN}10{RESET} points.")

    elif len(cs.intersection(ls)) == 2:
        print(f"You got {MAGENTA}2/5{RESET} numbers correct! Your final score is {GREEN}4{RESET} points.")

    elif len(cs.intersection(ls)) == 1:
        print(f"You got {MAGENTA}1/5{RESET} numbers correct.. not bad! Your final score is {GREEN}1{RESET} point.")

    else:
        print(f"Um... wow. You got {MAGENTA}none{RESET} of them correct. Maybe next time! Your final score is {GREEN}0{RESET} points.")

def program():

    global play, c_number_list, lucky_numbers

    while play == "y":
        lucky_numbers = random.sample(numbers, k=5)
        c_number_list = []

        while len(c_number_list) < 5 and play == "y":
            playing(display())
        
        chosen_set, lucky_set = sort(lucky_numbers)
        display2()
        result(chosen_set, lucky_set)

        play = input(f"\nWould you like to play again? Type {CYAN}Y{RESET} for yes and {CYAN}anything else{RESET} for no: ").lower()

    os.system("clear")
    print("Thank you for playing! We hope to see you again soon!")

program()
