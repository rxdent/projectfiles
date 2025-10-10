import os
os.system("clear")

def name():
    n = input("Please enter your name: ").capitalize()
    return n

def greeting(x):
    print(f"Welcome to temp converter, {x}!")

def faren(x):
    faren = input("Please enter a temperature in celsius: ")
    num = float(faren)
    print(f"{x}, {faren}°C is equal to {(num*9/5 + 32)}° Farenheit!")


def cels(x):
    cels = input("Please enter a temperature in fahrenheit: ")
    num = float(cels)
    print(f"{x}, {cels}°F is equal to {(num-32) * 5/9}")

def program():
    answer = "y"
    num = True
    temp = input("Would you like to convert to Celsius or Fahrenheit? Type F to convert to Farenheit. Type C to convert to celsius. To exit the program, type 'e': ").lower()

    while temp == "c" or temp == "f" or temp == "e":
        if temp == "f":
            while num:
                try:
                    os.system("clear")
                    faren(n)
                    num = False
                except ValueError:
                    os.system("clear")
                    input("Please type integers only. Press enter to continue..." )

        elif temp == "c":
            while num:
                try:
                    os.system("clear")
                    cels(n)
                    num = False
                except ValueError:
                    os.system("clear")
                    input("Please type integers only. Press enter to continue..." )

        elif temp != "c" or temp != "f" or temp != "e":
            input("Type c or f or e only. Press enter to continue...")
            program()

        answer = input("Do you want to convert a temperature again? Type y for yes and anything else for no: ")
        if answer == "y":
            os.system("clear")
            program()
        else:
            break
            

os.system("clear")
n = name()
greeting(n)
program()
os.system("clear")
print(f"Thank you for using temp converter, {n}! We hope to see you again soon!")
print("Program finished")

# Adding a comment for git purposes
    






