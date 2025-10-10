import os
os.system("clear")

#Colors ------------------------------------
GREEN =  "\033[32m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
BOLD = "\033[1m"
RESET = "\033[0m"

#Dictionaries/Lists ------------------------

produce = {"Apples by pound": 1.75, "Oranges per bag": 5.97, "Bananas per bunch": 1.32, "Carrot per bundle": 1.99, "Broccoli per bunch": 2.99, "Basil by bundle": 1.50, "Mint by bundle": 1.75, 
"Assorted herbs package": 3.85, "Cabbage head": 2.97, "Dozen of eggs": 3.97}

drinks = {"Milk": 3.04, "Low fat milk": 3.04, "Apple juice": 1.87, "Orange juice": 2.50, "Pack of soda (12)": 10.98, "1 soda can": 1.47, "Pack of water (12)": 3.97, "Bottle of water": 0.99,
"Iced coffee": 2.99, "Iced tea": 1.99}

baked_goods = {"Baguette": 1.97, "Sourdough loaf": 4.49, "Sliced white bread": 1.00, "Sliced whole wheat bread": 3.64, "Muffins (4 pack)": 4.56, "Cake": 5.98, "Cookies (12)": 3.64, "Croissant": 2.50,
"Bagels (12)": 4.82, "Tortillas (10)": 3.97}

cleaning_supplies = {"Dish soap": 2.99, "Laundry detergent": 8.97, "All purpose cleaner (lemon scented)": 3.65, "Rubber gloves": 3.91, "Sponge (3 pack)": 4.50, "Scrub brush": 1.50, "Paper towels (6 roll)": 7.12,
"Trash bags (30)": 14.99, "Toilet paper (12 roll)": 9.97, "Air freshener": 4.97}

snacks = {"Chips (party size)": 4.97, "Chocolate bar": 1.50, "Granola bar": 1.25, "Trail mix": 3.97, "Popcorn (microwaveable 12 pack)": 6.50, "Pretzels": 2.99, "Cheez-it": 4.49, "Gummy bears": 2.50,
"Cheetos": 3.97, "Chex mix": 5.49}

clothes = {"T-shirt": 9.97, "Jeans": 19.99, "Hoodie": 25.50, "Winter jacket": 49.99, "Sneakers": 59.97, "Socks (3 pack)": 5.97, "Hat": 14.99, "Swimsuit": 29.99, "Sunglasses": 11.58,
"Belt": 12.99}

pet_supplies = {"Dog kibble (small bag)": 19.99, "Dog treats (bag)": 14.28, "Cat food (small bag)": 14.99, "Cat food (Wet food, 32 pack)": 24.99, "Dog leash": 9.97, "Cat toy": 4.97, "Dog toy": 4.97,
"Litter": 9.80, "Bird food": 5.99, "Fish food": 3.97}

categories = ["Produce", "Drinks", "Baked goods", "Cleaning supplies", "Snacks", "Clothes", "Pet supplies"]

categories_data = [produce, drinks, baked_goods, cleaning_supplies, snacks, clothes, pet_supplies] #holds variables of the dictionaries to access easily.

cart = []
total = []

yes = True

#Code --------------------------------------

name = input("Hello, what's your name?: ")
input(f"\nWelcome to {CYAN}Jasmine's groccery store!{RESET} My name is Jasmine, it's nice to meet you, {name.capitalize()}! Our store has many selections to choose from, at low prices. Press enter to continue...")

playing = True

while playing:

    os.system("clear")

    print("Please choose a selection by typing in the number that corresponds to the section. Type anything else to exit the groccery store.\n")
    separator = ", "
    print(f"Cart: {separator.join(cart)}")
    print(f"Total: {round(sum(total), 2)}")
    print()

    #Choose a cateagory

    for index, categories_names in enumerate(categories, start=1): #turn categories list into indexed list.
        print(f"{MAGENTA}{index}{RESET} - {categories_names}\n")

    selection = input("Selection: ")
    
    if selection.isdigit() and 1 <= int(selection) <= len(categories): #If input is a digit, is greater or equal to 1 but is less than the length of the categories list.
        
        chosen_selection = categories_data[int(selection)-1] #assigns the inputed selection to the dictionary in categories_data. -1 because the index starts at 0.

        os.system("clear")
        print("Choose an item from the shelf!")

    #Choose an item
        while yes == True:
            for index, item_n in enumerate(chosen_selection, start=1): #turn selected category into indexed list.
                print()
                print(f"{MAGENTA}{index}{RESET} - {item_n}")
            
            print()
            try:

                item = int(input("Selection: "))
                item_names = list(chosen_selection) #convert dictionary into list to access indexes.)
                price = item_names[item - 1]  # -1 cause list starts at 0.
                yes = False

            except:
                os.system("clear")
                input("That is not an option, please type in numbers corresponding to only the given items. Press enter to continue...")
        
        yes = True

        os.system("clear")
        
        add = input(f"The price of {CYAN}{BOLD}{price}{RESET} is {GREEN}{BOLD}${chosen_selection[price]}{RESET}. Would you like to add this to your cart? Type Y for yes and anything else if no: ").lower()

        os.system("clear")

        if add == "y":
            cart.append(price)
            total.append(chosen_selection[price])
            print(f"{price} was added to the cart!")
            shop = input(f"Would you like to continue shopping? Press enter to continue and type N if you want to check out: ").lower()
            
            if shop == "n":
                os.system("clear")
                check_out = input(f"Your total is {GREEN}{round(sum(total), 2)}{RESET}. Would you like to check out? Type Y if yes and anything else if no: ").lower()

                if check_out == "y":
                    os.system("clear")
                    print("*beep* *beep* *puts items in bags*. Alright, done! Thank you for shopping at Jasmine's groccery store, I hope you have a great day!")
                    playing = False

    elif int(selection) > len(categories):
        os.system("clear")
        input("Please only type in a number corresponding to the given selections. Press enter to continue...")


    else:
        os.system("clear")
        print("Thank you for visiting Jasmine's groccery store! We hope you have a great day!")
        playing = False
        
        
#add if you want to add multiple of an item
#add if you want to check out but not add more items in category selection
#add if you want to remove items (multiple as well if you have multiple of an item)
#add you have a debit card and can only buy so many things
#add if you want to not choose an item and instead go back to the category selection screen
#add colors and etc so its easier to read
#add rest of comments so code is easier to read CAUSE IT'S CONFUSING TO LOOK AT
#add you can only type numbers when selecting something and it wont work with anything else, same with when saying yes or no.