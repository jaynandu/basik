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



# 6-1: Person
# Use a dictionary to store information about a person you know.
#  Store their first name, last name, age, and the city in which they live. 
# You should have keys such as first_name, last_name, age, and city. 
# Print each piece of information stored in your dictionary.

person = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 43,
    'city': 'sitka',
    }

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])
# Output:

# eric
# matthes
# 43
# sitka
# top

# 6-2: Favorite Numbers
# Use a dictionary to store people’s favorite numbers.
#  Think of five names, and use them as keys in your dictionary. 
# Think of a favorite number for each person, and store each as a value in your dictionary. 
# Print each person’s name and their favorite number.
#  For even more fun, poll a few friends and get some actual data for your program.

favorite_numbers = {
    'mandy': 42,
    'micah': 23,
    'gus': 7,
    'hank': 1000_000,
    'maggie': 0,
    }

num = favorite_numbers['mandy']
print(f"Mandy's favorite number is {num}.")

num = favorite_numbers['micah']
print(f"Micah's favorite number is {num}.")

num = favorite_numbers['gus']
print(f"Gus's favorite number is {num}.")

num = favorite_numbers['hank']
print(f"Hank's favorite number is {num}.")

num = favorite_numbers['maggie']
print(f"Maggie's favorite number is {num}.")
# Output:

# Mandy's favorite number is 42.
# Micah's favorite number is 23.
# Gus's favorite number is 7.
# Hank's favorite number is 1000000.
# Maggie's favorite number is 0.
# top

# 6-3: Glossary
# A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

# Think of five programming words you’ve learned about in the previous chapters. 
# Use these words as the keys in your glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output. 
# You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. 
# Use the newline character ('\n') to insert a blank line between each word-meaning pair in your output.
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }

word = 'string'
print(f"\n{word.title()}: {glossary[word]}")

word = 'comment'
print(f"\n{word.title()}: {glossary[word]}")

word = 'list'
print(f"\n{word.title()}: {glossary[word]}")

word = 'loop'
print(f"\n{word.title()}: {glossary[word]}")

word = 'dictionary'
print(f"\n{word.title()}: {glossary[word]}")
# Output:

# String: A series of characters.

# Comment: A note in a program that the Python interpreter ignores.

# List: A collection of items in a particular order.

# Loop: Work through a collection of items, one at a time.

# Dictionary: A collection of key-value pairs.
# top

# 6-4: Glossary 2
# Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print statements with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.

# Key concept to memorize

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
    }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")
# Output:

# Dictionary: A collection of key-value pairs.

# String: A series of characters.

# Boolean Expression: An expression that evaluates to True or False.

# Comment: A note in a program that the Python interpreter ignores.

# Value: An item associated with a key in a dictionary.

# Loop: Work through a collection of items, one at a time.

# List: A collection of items in a particular order.

# Conditional Test: A comparison between two values.

# Key: The first item in a key-value pair in a dictionary.

# Float: A numerical value with a decimal component.
# top

# 6-5: Rivers
# Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# Use a loop to print the name of each river included in the dictionary.
# Use a loop to print the name of each country included in the dictionary.

rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print(f"- {country.title()}")
# Output*:

# The Mississippi flows through United States.
# The Yangtze flows through China.
# The Fraser flows through Canada.
# The Nile flows through Egypt.
# The Kuskokwim flows through Alaska.

# The following rivers are included in this data set:
# - Mississippi
# - Yangtze
# - Fraser
# - Nile
# - Kuskokwim

# The following countries are included in this data set:
# - United States
# - China
# - Canada
# - Egypt
# - Alaska
# *Sometimes we like to think of Alaska as our own separate country.

# top

# 6-6: Polling
# Use the code in favorite_languages.py (page 104).

# Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
# Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")

coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']
for coder in coders:
    if coder in favorite_languages.keys():
        print(f"Thank you for taking the poll, {coder.title()}!")
    else:
        print(f"{coder.title()}, what's your favorite programming language?")
# Output:

# Jen's favorite language is Python.
# Sarah's favorite language is C.
# Phil's favorite language is Python.
# Edward's favorite language is Ruby.


# Thank you for taking the poll, Phil!
# Josh, what's your favorite programming language?
# David, what's your favorite programming language?
# Becca, what's your favorite programming language?
# Thank you for taking the poll, Sarah!
# Matt, what's your favorite programming language?
# Danielle, what's your favorite programming language?
# top

# 6-7: People
# Start with the program you wrote for Exercise 6-1 (page 102). Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

# Make an empty list to store people in.
people = []

# Define some people, and add them to the list.
person = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 46,
    'city': 'sitka',
    }
people.append(person)

person = {
    'first_name': 'lemmy',
    'last_name': 'matthes',
    'age': 2,
    'city': 'sitka',
    }
people.append(person)

person = {
    'first_name': 'willie',
    'last_name': 'matthes',
    'age': 11,
    'city': 'sitka',
    }
people.append(person)

# Display all of the information in the dictionary.
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()
    
    print(f"{name}, of {city}, is {age} years old.")
# Output:

# Eric Matthes, of Sitka, is 46 years old.
# Lemmy Matthes, of Sitka, is 2 years old.
# Willie Matthes, of Sitka, is 11 years old.
# top

# 6-8: Pets
# Make several dictionaries, where the name of each dictionary is the name of a pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do print everything you know about each pet.

# Note: When I decided to post solutions and wrote complete programs to solve each exercise, I realized this problem was not as well phrased as it should have been. It doesn’t really make sense to name each dictionary for the pet it describes; that information should really be included in the dictionary, rather than being used as the name of the dictionary. This solution reflects that approach.

# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")
# Output:

# Here's what I know about John:
#     animal type: python
#     name: john
#     owner: guido
#     weight: 43
#     eats: rats

# Here's what I know about Clarence:
#     animal type: chicken
#     name: clarence
#     owner: tiffany
#     weight: 2
#     eats: seeds

# Here's what I know about Peso:
#     animal type: dog
#     name: peso
#     owner: eric
#     weight: 37
#     eats: shoes
# top

# 6-9: Favorite Places
# Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exericse a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.

favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'erin': ['hawaii', 'iceland'],
    'willie': ['mt. verstovia', 'the playground', 'new hampshire']
    }

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")
# Output:

# Eric likes the following places:
# - Bear Mountain
# - Death Valley
# - Tierra Del Fuego

# Erin likes the following places:
# - Hawaii
# - Iceland

# Willie likes the following places:
# - Mt. Verstovia
# - The Playground
# - New Hampshire
# top

# 6-10: Favorite Numbers
# Modify your program from Exercise 6-2 (page 102) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.

favorite_numbers = {
    'mandy': [42, 17],
    'micah': [42, 39, 56],
    'gus': [7, 12],
    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f"  {number}")
# Output:

# Micah likes the following numbers:
#   42
#   39
#   56

# Mandy likes the following numbers:
#   42
#   17

# Gus likes the following numbers:
#   7
#   12
# top

# 6-11: Cities
# Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

cities = {
    'santiago': {
        'country': 'chile',
        'population': 6_310_000,
        'nearby mountains': 'andes',
        },
    'talkeetna': {
        'country': 'united states',
        'population': 876,
        'nearby mountains': 'alaska range',
        },
    'kathmandu': {
        'country': 'nepal',
        'population': 975_453,
        'nearby mountains': 'himilaya',
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()

    print(f"\n{city.title()} is in {country}.")
    print(f"  It has a population of about {population}.")
    print(f"  The {mountains} mounats are nearby.")
# Output:

# Santiago is in Chile.
#   It has a population of about 6310000.
#   The Andes mounats are nearby.

# Talkeetna is in United States.
#   It has a population of about 876.
#   The Alaska Range mounats are nearby.

# Kathmandu is in Nepal.
#   It has a population of about 975453.
#   The Himilaya mounats are nearby.
# top