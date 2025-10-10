import os
os.system("clear")

#Variables -----------------------------

pokemon_dict = {"Pikachu": "an electric type mouse pokemon.", "Bulbasaur": "some sort of frog looking grass type pokemon.", "Charmander": "a fire type lizard pokemon.", "Squirtle": "a water type turtle pokemon."}

pokemon_dict_list = list(pokemon_dict)

pokemon = ["Pikachu", "Bulbasaur", "Charmander", "Squirtle"]

answer = "n"

#Code ----------------------------------

name = input("What is your name?: ")

os.system("clear")

start = input(f'Welcome to the Pokemon Center, {name.capitalize()}! You are finally old enough to choose your first pokemon. We have many options. Would you like to see? Type "start" to continue: ').lower()

while start == "start":

    while answer == "n":

        os.system("clear")
        print("Type the number corresponding to the pokemon to learn more! Choose wisely...\n")

        for index, item in enumerate(pokemon, start=1):

            print(f"{index} - {item}\n")

        selection = (input("\nSelection: "))

        if selection.isdigit() and int(selection) <= len(pokemon):

            chosen_pokemon = (pokemon_dict_list[int(selection)-1])

            os.system("clear")

            print(f"""You have selected: {chosen_pokemon}.\n\n{chosen_pokemon} is {pokemon_dict[pokemon[int(selection)-1]]}\n""")
            
            answer = input(f"Would you like to select {chosen_pokemon}? Press enter for yes or N for no: ").lower()
        
        else:
            os.system("clear")
            input("Only type in numbers corresponding to the pokemon! Press enter to continue...")

    os.system("clear")
    print(f"Congrats {name}! {chosen_pokemon} is yours, treat them well and have a good adventure!")
    break