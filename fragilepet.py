import os
import random
import time
os.system("clear")

pets = ["Cigarette-smoking mouse", "Germaphone cat", "Clingy dog", "Attention-seeking bird"]
pets_dict = {"Cigarette-smoking mouse": "This mouse is heavily addicted to nicotine. Mouse will never care about cleanliness levels but your money will slowly deplete from Mouse's smoking habits.",
"Germaphone cat": "This cat is scared of even a speck of mud. If your cleanliness levels reach 50%, you die. On the flipside, Cat will always entertain itself so it's fun levels won't go down.",
"Clingy dog": "This dog always needs your love and affection and it's fun levels go down faster than the other pets. However, Dog will never cause trouble for you.",
"Attention-seeking bird": "This bird will do everthing in it's power to make yoru life more difficult. Fortunately, it's bathroom levels will never go down because Bird just goes anywhere."}

pets_dict_list = list(pets_dict) #makes it a list so I can access the index.

events = {

    "housefire": {"desc": "Your pet was cooking at the stove and caused a house fire that heavily damaged your kitchen! Your pet's cleanliness went down by 70, and you lost $50.", "cost": -50, "cleanliness": -70},
    "gambling": {"desc": "Your pet was gambling and lost a lot of your money! You lost $100.", "cost": -100},
    "pet god": {"desc": "The pet gods have decided that your pet has been alive for too long and is trying to kill him! All levels went down by 50.", "hunger": -50, "fun": -50, "cleanliness": -50, "bathroom": -50},
    "binge-eat": {"desc": "Your pet ate all the food in the house so you had to go out and buy more! You lost $25.", "cost": -25, }

}

events_list = list(events)

h = 100 #hunger
f = 100 #fun
c = 100 #cleanliness
b = 100 #bathroom
money = 150

pet_food = []

stats = { 
    "hunger": "h",
    "fun": "f",
    "cleanliness": "c",
    "bathroom": "b",
    "cost": "money"
    }

def choose_pet():
    os.system("clear")

    choosing = True
    while choosing:
        os.system("clear")
        print("Select a pet by typing in the corresponding number: \n")

        for index, pet in enumerate(pets_dict, start=1):
            print(f"{index} - {pet}")

        choice = input("\nChoice: ")

        if choice.isdigit() and int(choice) <= len(pets):
            os.system("clear")
            print(f"You have selected {pets[int(choice)-1]}. {pets_dict[pets[int(choice)-1]]}")
            yn = input("\nDo you want this pet? Type y for yes and anything else for no: ").lower()
            if yn == "y":
                chosen_pet = pets_dict_list[int(choice)-1]
                input(f"\nYou have selected {pets[int(choice)-1]}. Good luck. You're going to need it. Press enter to continue...")
                break

        else:
            os.system("clear")
            input("Only type in numbers correspoding to the following pets. Press enter to continue...")
            os.system("clear")

    return chosen_pet #int of the dict list

def base_system():
    global h, f, c, b, money, pet_food
    print(f"""\nYour stats:
Hunger: {h}
Fun: {f}
Cleanliness: {c}
Bathroom: {b}
Wallet: ${money}""")

    while h > 0 and f > 0 and c > 0 and b >0:
        task = input("Task: ").lower

        if task == "feed":
            print(f"Your food: {pet_food}\n")
            print("Select something from the shelf!")

        elif task == "play":
            f = +15
            print(f"You played with pet! Pet's fun level went up by 15.")

        elif task == "bath":
            c = +30
            print("You bathed pet! Pet's cleanliness level went up by 30.")

        elif task =="take outside":
            b = +50
            print("You let pet outside... pets bathroom level went up by 50.")

        else:
            continue

def randevent(): #FIGURE THIS OUT LATER
    global h, f, c, b, money 

    event_key = random.choice(events_list)
    event = events[event_key] #accesses the values inside the dictionary from the randomly selected event.
    print(event["desc"])

    for key, value in event.items(): #for every value in the randomly selected key
        if key in stats: #if the key of the event is in the stats
            var_name = stats[key] #access the value inside the key
            globals()[var_name] += value #and and or subtract the amount from value. THIS CHANGES THE GLOBAL VARIABLE
    print(f"""\nYour stats:
Hunger: {h}
Fun: {f}
Cleanliness: {c}
Bathroom: {b}
Wallet: ${money}""")



def eventintervals():
    intervals = random.uniform(5,30) #seconds between each event
    time.sleep(intervals)
    os.system("clear")
    print("EVENT OCCURING...\n")
    randevent()




def program():
    input("Welcome to FRAGILE PET. Anything and everything is trying to kill your pet, so make sure you keep your pets need cared for, and try to avoid any sudden events! Press enter to continue...")
    os.system("clear")
    input("""Directions: You have 4 levels that you always have to make sure never hit 0. There are ways to avoid this.

Hunger: Go to the store and buy food for your pet.
Fun: Play with your pet.
Cleanliness: Give your pet a bath.
Bathroom: Take your pet outside.

You can also buy potions in the shop to restore these values.

You need money to buy things, so go to work! You must bring your pet with you, and who knows what mischief they'll get into...

Commands:
"feed" = Feed pet
"play" = Play with pet
"bath" = bathe pet
"take outside" = Let pet use the bathroom
"work" = Go to work

Press enter to continue """)

    global n
    os.system("clear")
    n = input("\nEnter your name: ")

    choose_pet()
    randevent()




program()
