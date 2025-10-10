# #Strings

# print("Hello World!")

# #delete hashtags if you want to see demo.

# #dialog = "You can use double or single quotes to talk"
# #dialog2 = "However, you can't use it more than twice."
# #dialog3 = "For example: "Hi!" my name is Jasmine." #see how the dialog isn't in blue?
# #dialog4 = 'This doesn't work either.'
# #dialog5 = "So use both to avoid these issue's " + 'Ya "hear?"'

# #You can also do this for long strings! use 3 quotes

# dialog6 = """

# Somebody's Heine
# is crowding my icebox

# Somebody's cold one
# is giving me chills
# """
# print(dialog6)

# #Expressions

# print("apple" * 5) #This prints apple 5 times

# #Variables

# price = 10 #Very similar to javascript, just without var.

# # + is for adding
# # - subtracting
# # * multiplying
# # / dividing
# # ** exponent
# # // floor division
# # % shows if a number can go into another number (ex 2 can go into 4.) 0 = even. 1 = odd
# #Python goes in the order of operations. PEMDAS
# # abs(number) absolute value
# # round(number) rounds number. you can add more than one number (ex: round(number, number))

# print(price) #prints variable

# #all rules for var in javascript are the same for python.

# float = 4.9 #integers with decimals are called floating point numbers, or floats for short

# is_published = True #Boolean values. MUST USE CAPITAL FIRST LETTER. Use true or false

# #use an underscore to seperate words!!

# #Input (equivalent of prompt)

# name = input("What is your name?")
# print("Nice to meet you " + name + "!")

# #instead of using a + sign, you can also do this..

# greeting = "Nice to meet you,"

# message = "{} {}! Glad to see you!".format(greeting, name) #creates a format and looks neater.
# print(message)

# #see line 92 for another way to also do this using the f method.

# #type conversions

# #float() converts a value into a number with a decimal point (ex: float(3) = 3.0)
# #int() converts string into an integer
# #bool() converts a string into a boolean value

# weight = input("What is your weight in pounds?")
# kilo = int(weight)/2.205
# print("Your weight is " + str(kilo)) #You have to convert integers to strings in order to use string concantation


# #Lists

# #Lists are EXACTLY the same as javascript

# listy = "Hello"
# print(listy[0]) #prints the first letter in the string
# print(listy[-1]) #prints the last letter in the string and so on
# print("School is " + listy[0:4]) # The ":" pulls all the characters between those indexes

# print(listy[1:]) #Excludes first letter. Can do it visa versa for last letter as well.

# copy = listy[:] #creates a copy of your variable as it takes all characters

# first = input("What is your first name?")
# last = input("What is your last name?")
# print("Your initials is: " + first[0] + last[0] )

# #You can also use a colon if you want to copy more than 1 letter.

# nickname = (first[0:3])
# print("Your nickname is " + nickname)

# #Formatted strings (equivalent of template literal on javascript)

# message = f"{first} [{last}]" #allows coder to use brackets without it become a list. can use on other things as well.
# print(message)

# #Lists

# print(len(first)) #shows how many assets are in a string.
# groccery = ["apples", "bannanas", "oranges"]
# print(len(groccery)) #can be used on lists as well
# groccery.append("tomatoes") #adds to end of list. use an index plus a comma if you want it in a specific spot.
# #using .extend can allow you to add another list to the end of a list.
# groccery.remove("apples")
# groccery.pop() #removes last value in the list
# print(groccery)
# # .reverse, reverses the list. .sort sorts it by alphabetical order.
# #using .sort(reverse==true) will reverse whatever you sorted
# #using sorted() or reversed() will alter the list without changing the og list
# #use print(sum, min, max(num)) to get the desired output
# print(groccery.index("oranges")) #tells you where an item is on a list
# #use the IN method to see if a value is in a list.
# print("watermelom" in groccery)
# for index, groccery in enumerate(groccery, start=1):
#     print(index, groccery)

# #typing in enumerate adds its value to the printed list. Adding index will remove the '' on the values
# #using start= will print out the list's index as your desired #. if you don't use it it just starts at 0.
# groccery = ["apples", "bannanas", "oranges"]
# groccery_str = "-".join(groccery)
# print(groccery_str)


# #String methods

# pop = "pop"
# print(pop.upper()) #makes all characters uppercase. You can also use .lower for lowercase
# print(pop.find("o")) #Finds where a value is in a string
# print(pop.replace("pop", "bang")) #replaces values in a string, not permanently.
# print("pop" in pop) #checks if value is in a string. Boolean expression
# print(pop.count('p')) #counts how many times a letter shows in a string. Also works if you input words instead of letters.
# print(dir(pop))  #shows all methods available to the variable your using

# print(type(pop)) #shows what type of class a variable is.

# #use print(help(asdasdasdadasd)) and type in a method or function if you need help



#Datetime module

import datetime

tday = datetime.date.today() #gives you todays date
print(tday)
print(datetime.date(2016,5,8)) #whatever date you want.
print(tday.weekday()) #Monday 0 - Sunday 6
print(tday.isoweekday()) #Monday 1 - Sunday 7

tdelta = datetime.timedelta(days=7) #makes a difference in dates
print(tday + tdelta) #calculates distance
#This will print a date 1 week now from today's date.
#.now gives you the datetime of whatever timezone you want: ex.utcnow