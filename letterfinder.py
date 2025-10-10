#theme is characters from The Legend of Zelda, any game.
import random
import os
os.system("clear")

GREEN = "\033[32m"
MAGENTA = "\033[35m"
RESET = "\033[0m"
RED = "\033[31m"



start = input(f"""Welcome to the game {GREEN}Letter Finder: The Legend of Zelda{RESET} characters edition.
The rules are simple. Guess a letter in the word until you guess the word correctly! For each letter you guess incorrectly you only get 5 tries, then game over.
You also get 1 hint per word. Type: "hint" to get your hint.
Have fun and good luck! Type: "{MAGENTA}start{RESET}" to play the game! Type "{MAGENTA}exit{RESET}" to exit the game.: """).lower()

while start == "start":

    option = ["link", "zelda", "ganon", "hylia", "beedle", "impa", "navi", "mipha", "urbosa", "daruk"]
    hint = ["The main character", "Her name in in the title of the game", "The main bad character", "The goddess of ___", "Has a large backpack", "Part of the sheikah tribe", "It's a fairy", "She's a fish", "She's really tall", "He eats rocks"]
    guesses = []
    word = random.choice(option)
    wordindex = option.index(word)
    wordList = list(word)
    tries = (len(wordList)-1)
    display = list(len(word) * ["_"])

    while tries != 0 and "".join(display) != word:

        print(f"{RED}Incorrect letters guessed{RESET}:")
        print(guesses)
        print(f"{GREEN}{display}{RESET}")
        letter = input("Guess a letter in the word!: ").lower()
        
        if letter == "hint":
            print(f"Hint: {hint[wordindex]}")
        
        found_letter = False

        for i in range(len(wordList)):

            if wordList[i] == letter:
                display[i] = letter
                found_letter = True

            if letter in guesses:
                print(f"Already guessed the letter: {MAGENTA}{letter}{RESET}. Please choose another letter!")
                break

        if found_letter == False:
            guesses.append(letter)
            print(f"You have {RED}{tries} tries{RESET} remaining.")
            tries -= 1
            
        elif tries == 0:
            break
        
    if tries == 0:
        print(display)
        start = input(f'{RED}You are out of tries.. Game over!{RESET} The character was: "{MAGENTA}{word.capitalize()}{RESET}" Would you like to play again? Type "start" to play again. Type "exit" to exit the game: ')

    elif "".join(display) == word:
        print(f"{MAGENTA}{display}{RESET}")
        start = input(f'Congrats, you guessed the character: "{MAGENTA}{word.capitalize()}{RESET}"! Would you like to play again? Type "{MAGENTA}start{RESET}" to play again. Type "{MAGENTA}exit{RESET}" to exit the game: ').lower()

    if start == "exit":
        print(f"Thank you for playing {GREEN}Letter Finder: The Legend of Zelda{RESET} characters edition! We hope to see you again soon!")
        break