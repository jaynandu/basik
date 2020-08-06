# Solutions - Chapter 4
# 4-1: Pizzas
# 4-3: Counting to Twenty
# 4-5: Summing a Million
# 4-7: Threes
# 4-8: Cubes
# 4-9: Cube Comprehension
# 4-11: My Pizzas, Your Pizzas
# 4-13: Buffet
# Back to solutions.

# 4-1: Pizzas
# Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.

# Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
# Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
# favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']

# Print the names of all the pizzas.
for pizza in favorite_pizzas:
    print(pizza)

print("\n")

# Print a sentence about each pizza.
for pizza in favorite_pizzas:
    print(f"I really love {pizza} pizza!")

print("\nI really love pizza!")
# Output:

# pepperoni
# hawaiian
# veggie


# I really love pepperoni pizza!
# I really love hawaiian pizza!
# I really love veggie pizza!

# I really love pizza!
# top

# 4-3: Counting to Twenty
# Use a for loop to print the numbers from 1 to 20, inclusive.

numbers = list(range(1, 21))

for number in numbers:
    print(number)
# Output:

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# top

# 4-5: Summing a Million
# Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts
# at one and ends at one million. Also, use the sum() function to see
# how quickly Python can add a million numbers.

numbers = list(range(1, 1_000_001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))
# Output:

# 1
# 1000000
# 500000500000
# top

# 4-7: Threes
# Make a list of the multiples of 3 from 3 to 0. Use a for loop to print the numbers in your list.

threes = list(range(3, 31, 3))

for number in threes:
    print(number)
# Output:

# 3
# 6
# 9
# 12
# 15
# 18
# 21
# 24
# 27
# 30
# top

# 4-8: Cubes
# A number raised to the third power is called a cube.
#  For example, the cube of 2 is written as 2**3 in Python.
#  Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10),
# and use a for loop to print out the value of each cube.

cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)
# Output:

# 1
# 8
# 27
# 64
# 125
# 216
# 343
# 512
# 729
# 1000
# top

# 4-9: Cube Comprehension
# Use a list comprehension to generate a list of the first 10 cubes.

cubes = [number**3 for number in range(1, 11)]

for cube in cubes:
    print(cube)
# Output:

# 1
# 8
# 27
# 64
# 125
# 216
# 343
# 512
# 729
# 1000
# top

# 4-11: My Pizzas, Your Pizzas
# Start with your program from Exercise 4-1 (page 60).
# Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:

# Add a new pizza to the original list.
# Add a different pizza to the list friend_pizzas.
# Prove that you have two separate lists. Print the message, My favorite pizzas are:,
# and then use a for loop to print the first list. Print the message, My friend’s favorite pizzas are:,
# and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("meat lover's")
friend_pizzas.append('pesto')

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")
# Output:

# My favorite pizzas are:
# - pepperoni
# - hawaiian
# - veggie
# - meat lover's

# My friend's favorite pizzas are:
# - pepperoni
# - hawaiian
# - veggie
# - pesto
# top

# 4-13: Buffet
# A buffet-style restaurant offers only five basic foods.
# Think of five simple foods, and store them in a tuple.

# Use a for loop to print each food the restaurant offers.
# Try to modify one of the items, and make sure that Python rejects the change.
# The restaurant changes its menu, replacing two of the items with different foods.
# Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'salmon burger', 'crab cakes',
)

print("You can choose from the following menu items:")
for item in menu_items:
    print(f"- {item}")

menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'black cod tips', 'king crab legs',
)

print("\nOur menu has been updated.")
print("You can now choose from the following items:")
for item in menu_items:
    print(f"- {item}")
# Output:

# You can choose from the following menu items:
# - rockfish sandwich
# - halibut nuggets
# - smoked salmon chowder
# - salmon burger
# - crab cakes

# Our menu has been updated.
# You can now choose from the following items:
# - rockfish sandwich
# - halibut nuggets
# - smoked salmon chowder
# - black cod tips
# - king crab legs
# top


# IF statement


# 5-3: Alien Colors  # 1
# Imagine an alien was just shot down in a game.
# Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

# Write an if statement to test whether the alien’s color is green.
# If it is , print a message that the player just earned 5 points.

# Write one version of this program that passes the if test and another tha fails.
#  (The version that fails will have no output.)

# Passing version:

alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")
# Output:

# You just earned 5 points!
# Failing version:

alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
# (no output)

# top

# 5-4: Alien Colors  # 2
# Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.

# If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
# If the alien’s color isn’t green, print a statement that the player just earned 10 points.
# Write one version of this program that runs the if block and another that runs the else block.
# if block runs:

alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

# Output:

# You just earned 5 points!
# else block runs:

alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")
# Output:

# You just earned 10 points!
# top

# 5-5: Alien Colors  # 3
# Turn your if-else chain from Exercise 5-4 into an if-elif-else cahin.

# If the alien is green, print a message that the player earned 5 points.
# If the alien is yellow, print a message that the player earned 10 points.
# If the alien is red, print a message that the player earned 15 points.
# Write three versions of this program, making sure each message is printed for the appropriate color alien.
alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

# Output for 'red' alien:

# You just earned 15 points!
# top

# 5-6: Stages of Life
# Write an if-elif-else cahin that determines a person’s stage of life. Set a value for the variable age, and then:

# If the person is less than 2 years old, print a message that the person is a baby.
# If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# If the person is at least 4 years old but less than 13, print a message that the person is a toddler.
# If the person is at least 13 years old but less than 20, print a message that the person is a toddler.
# If the person is at least 20 years old but less than 65, print a message that the person is a toddler.
# If the person is age 65 or older, print a message that the person is an elder.


age = 17

if age < 2:
    print("You're a baby!")
elif age < 4:
    print("You're a toddler!")
elif age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager!")
elif age < 65:
    print("You're an adult!")
else:
    print("You're an elder!")

# Output:

# You're a teenager!
# top

# 5-7: Favorite Fruit
# Make a list of your favorite fruits, and then write a series of independent
# if statements that check for certain fruits in your list.

# Make a list of your three favorite fruits and call it favorite_fruits.
# Write five if statements. Each should check whether a certain kind of fruit is in your list.
# If the fruit is in your list, the if block should print a statement, such as You really like bananas!


favorite_fruits = ['blueberries', 'salmonberries', 'peaches']

if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'apples' in favorite_fruits:
    print("You really like apples!")
if 'blueberries' in favorite_fruits:
    print("You really like blueberries!")
if 'kiwis' in favorite_fruits:
    print("You really like kiwis!")
if 'peaches' in favorite_fruits:
    print("You really like peaches!")


# Output:

# You really like blueberries!
# You really like peaches!
# top

# 5-8: Hello Admin
# Make a list of five or more usernnames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user:

# If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# Otherwise, print a generic greeting, such as Hello Eric, thank you for loggin in again.


usernames = ['eric', 'willie', 'admin', 'erin', 'ever']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for loggin in again!")


# Output:

# Hello eric, thank you for logging in again!
# Hello willie, thank you for logging in again!
# Hello admin, would you like to see a status report?
# Hello erin, thank you for logging in again!
# Hello ever, thank you for logging in again!
# top

# 5-9: No Users
# Add an if test to hello_admin.py to make sure the list of users is not empty.

# If the list is emtpy, print the message We need to find some users!
# Remove all of the usernames from your list, and make sure the correct message is printed.


usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for loggin in again!")
else:
    print("We need to find some users!")


# Output:

# We need to find some users!
# top

# 5-10: Checking Usernames
# Do the following to create a program that simulates how websites ensure that everyone has a unique username.

# Make a list of five or more usernames called current_users. Make another list of five usernames called new_users.
# Make sure one or two of the new usernames are also in the current_users list.
# Loop through the new_users list to see if each new username has already been used.
#  If it has, print a message that the person will need to enter a new username.
#  If a username has not been used, print a message saying that the username is available.
# Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.


current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that name is taken.")
    else:
        print(f"Great, {new_user} is still available.")


# Output:

# Great, sarah is still available.
# Sorry Willie, that name is taken.
# Great, PHIL is still available.
# Sorry ever, that name is taken.
# Great, Iona is still available.
# Note: If you’re not comfortable with list comprehensions yet, the list current_users_lower can be generated using a loop:

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())


# top

# 5-11: Ordinal Numbers
# Ordinal numbers indicate their position in a list, such as 1st or 2nd.
#  Most ordinal numbers end in th, except 1, 2, and 3.

# Store the numbers 1 through 9 in a list.
# Loop through the list.
# Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
# Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.


numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
# Output:

# 1st
# 2nd
# 3rd
# 4th
# 5th
# 6th
# 7th
# 8th
# 9th
# top
