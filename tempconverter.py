import os
os.system("clear")

name = input("Please enter your name: ")
answer = "Y"
print(f"Welcome to temp converter, {name}!")

while True:
    while (answer != "F" or answer!= "C" or answer!= "f" or answer!= "C"):
        temp = input("Would you like to convert to Celsius or Fahrenheit? Type F to convert to Farenheit. Type C to convert to celsius. To exit the program, type 'e':")
            
        if (temp == "F" or temp == "f"):
            try:
                faren = input("Please enter a temperature in celsius: ")
                num = float(faren)
                print(f"{name}, {faren}°C is equal to {(num*9/5 + 32)}° Farenheit!")
            except ValueError:
                print("Please type integers only." )

        elif (temp == "C" or temp == "c"):
            try:
                cels = input("Please enter a temperature in fahrenheit: ")
                num = float(cels)
                print(f"{name}, {cels}°F is equal to {(num-32) * 5/9}")
            except ValueError:
                print("Please type integers only.")
        elif (temp == "e"):
            break
            
        else:
            print("That is not a valid prompt. Please only enter C or F or e: ")

    answer = input("Are you sure you want to exit the program? Type Y for yes and N for no: ")

    if answer == "Y" or answer == "y":
        print(f"Thank you for using temp converter, {name}! We hope to see you again soon!")
        break