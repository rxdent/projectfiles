#Strings

print("Hello World!")

#delete hashtags if you want to see demo.

#dialog = "You can use double or single quotes to talk"
#dialog2 = "However, you can't use it more than twice."
#dialog3 = "For example: "Hi!" my name is Jasmine." #see how the dialog isn't in blue?
#dialog4 = 'This doesn't work either.'
#dialog5 = "So use both to avoid these issue's " + 'Ya "hear?"'

#You can also do this for long strings! use 3 quotes

dialog6 = """

Somebody's Heine
is crowding my icebox

Somebody's cold one
is giving me chills
"""
print(dialog6)

#Expressions

print("apple" * 5) #This prints apple 5 times

#Variables

price = 10 #Very similar to javascript, just without var.

# + is for adding
# - subtracting
# * multiplying
# / dividing
# ** exponent
# // floor division
# % shows if a number can go into another number (ex 2 can go into 4.) 0 = even. 1 = odd
#Python goes in the order of operations. PEMDAS
# abs(number) absolute value
# round(number) rounds number. you can add more than one number (ex: round(number, number))

print(price) #prints variable

#all rules for var in javascript are the same for python.

float = 4.9 #integers with decimals are called floating point numbers, or floats for short

is_published = True #Boolean values. MUST USE CAPITAL FIRST LETTER. Use true or false

#use an underscore to seperate words!!

#Input (equivalent of prompt)

name = input("What is your name?")
print("Nice to meet you " + name + "!")

#instead of using a + sign, you can also do this..

greeting = "Nice to meet you,"

message = "{} {}! Glad to see you!".format(greeting, name) #creates a format and looks neater.
print(message)

#see line 92 for another way to also do this using the f method.

#type conversions

#float() converts a value into a number with a decimal point (ex: float(3) = 3.0)
#int() converts string into an integer
#bool() converts a string into a boolean value

weight = input("What is your weight in pounds?")
kilo = int(weight)/2.205
print("Your weight is " + str(kilo)) #You have to convert integers to strings in order to use string concantation


#Lists

#Lists are EXACTLY the same as javascript

listy = "Hello"
print(listy[0]) #prints the first letter in the string
print(listy[-1]) #prints the last letter in the string and so on
print("School is " + listy[0:4]) # The ":" pulls all the characters between those indexes

print(listy[1:]) #Excludes first letter. Can do it visa versa for last letter as well.

copy = listy[:] #creates a copy of your variable as it takes all characters

first = input("What is your first name?")
last = input("What is your last name?")
print("Your initials is: " + first[0] + last[0] )

#You can also use a colon if you want to copy more than 1 letter.

nickname = (first[0:3])
print("Your nickname is " + nickname)

#Formatted strings (equivalent of template literal on javascript)

message = f"{first} [{last}]" #allows coder to use brackets without it become a list. can use on other things as well.
print(message)

#Lists

print(len(first)) #shows how many assets are in a string.
groccery = ["apples", "bannanas", "oranges"]
print(len(groccery)) #can be used on lists as well
groccery.append("tomatoes") #adds to end of list. use an index plus a comma if you want it in a specific spot.
#using .extend can allow you to add another list to the end of a list.
groccery.remove("apples")
groccery.pop() #removes last value in the list
print(groccery)
# .reverse, reverses the list. .sort sorts it by alphabetical order.
#using .sort(reverse==true) will reverse whatever you sorted
#using sorted() or reversed() will alter the list without changing the og list
#use print(sum, min, max(num)) to get the desired output
print(groccery.index("oranges")) #tells you where an item is on a list
#use the IN method to see if a value is in a list.
print("watermelom" in groccery)
for index, groccery in enumerate(groccery, start=1):
    print(index, groccery)

#typing in enumerate adds its value to the printed list. Adding index will remove the '' on the values
#using start= will print out the list's index as your desired #. if you don't use it it just starts at 0.
groccery = ["apples", "bannanas", "oranges"]
groccery_str = "-".join(groccery)
print(groccery_str)


#String methods

pop = "pop"
print(pop.upper()) #makes all characters uppercase. You can also use .lower for lowercase
print(pop.find("o")) #Finds where a value is in a string
print(pop.replace("pop", "bang")) #replaces values in a string, not permanently.
print("pop" in pop) #checks if value is in a string. Boolean expression
print(pop.count('p')) #counts how many times a letter shows in a string. Also works if you input words instead of letters.
print(dir(pop))  #shows all methods available to the variable your using

print(type(pop)) #shows what type of class a variable is.

#use print(help(asdasdasdadasd)) and type in a method or function if you need help

#tuples are just lists that are immutable (cannot be altered). You use () instead of [] to create it.

tuple_1 = ("water", "juice", "soda", "milk")
print(tuple_1)

#sets are like lists but they are unordered and change every time. You can compare them with other setsas well.

set_1 = {"fantasy", "action", "sci-fi", "romance"}
set_2 = {"history", "informational", "romance", "sci-fi"}

print(set_1.intersection(set_2)) #Shows similarities between sets
print(set_1.difference(set_2)) #Shows differences between sets
print(set_1.union(set_2)) #combines sets together but does not dupilcate same values

#dictionaries create variables with multiple values, strs, ints, lists, anything.

student = {"name": "Jasmine", "age": 16, "grade": 11}

print(student)
print(student["name"]) #prints whatever your looking for
print(student.get("purple")) #sees if a value is there. this will come up as "none"
student.update({"name": "Laila"}) #changes a value
print(student)

#del student[""] deletes a value
#you can also use .update or var["stuff"] = "new value" to add new values
#the difference between del and .pop is that delete actually deletes the value, pop removes it, but the value can still be accessed
#dictionary refers to the variable. Keys refer to all the catagories your using, values are what go inside the keys, and items are the values and keys combined. ex(name: Jasmine)
#you can use .keys, .values, etc, to access just what your looking for, not the whole dictionary.

#booleans
#check true and false values

#for ex, and statements check if both values are true:
a = 1
b = 2
if a + b == 3 and b - 1 == 1:
    print("hey")

#or statements check if at least 1 value is true
if a == 1 or b == 4:
    print("What's up?")

#not statements check if a value is false. is checks if a value is equal to what you input
if a is not b:
    print("How's it going?")
#you can mix and match all of them!

#for loops

nums = [1,2,3,4,5]

for num in nums: #for every number in nums
    if num == 3: #if num is equal to 3
        print("Three")
        break #end the loop
    print(num) #if num is not equal to 3 print the rest of the numbers.

for num in nums: 
    if num == 3: 
        print("Three")
        continue #prints out the three at 3 but continues the loop.
    print(num)

#Methods (functions):

def hello_funct():
    print("Hello function!")

hello_funct()

def name():
    n = input("Name? ") # n is a local variable. you cannot access this outside this function
    return n


def greeting(x):
    print(f"Hello {x}")


def program():
    greeting(name())
    decision = input("Again? ")
    if decision == "y":
        program() #You can put functions inside functions.

program()

#Slicing

