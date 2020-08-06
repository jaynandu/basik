# String
message = "I learn coding"
print(message)

name = "ada lovelace"
print(name.title())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello,{full_name.title()}!")

name = "Eric"
message = f"Hello {name}, would you like to learn some Python today?"
print(message)

name = "ALBERT"
name1 = "Robert"
name2 = "vido"
print(name.lower())
print(name1.upper())
print(name2.title())


quote = 'Albert Eistein once said,"A person who never made a mistake never tried anything new. " '
print(quote)

4/2

3.0**2

# List

universe_age = 12_000_000
print(universe_age)

bicycles = ['trek', 'canondale', 'redline', 'specialized']
print(bicycles[0].title())
print(bicycles[3].upper())

motorcylces = ['honda', 'yamaha', 'suzuki']
last_owned = motorcylces.pop(1)
print(f"The last motorcycle I owned was a {last_owned.title()}.")


# First test resolution
# Manipulation of the Guest list# Invite some people to dinner.
guests = ['guido van rossum', 'jack turner', 'lynn hill']

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

# Jack can't make it! Let's invite Gary instead.
del(guests[1])
guests.insert(1, 'gary snyder')

# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

# We got a bigger table, so let's add some more people to the list.

print("\nWe got a bigger table!")
guests.insert(0, 'frida kahlo')
guests.insert(2, 'reinhold messner')
guests.append('elizabeth peratrovich')

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[3].title()
print(f"{name}, please come to dinner.")

name = guests[4].title()
print(f"{name}, please come to dinner.")

name = guests[5].title()
print(f"{name}, please come to dinner.")

# Perso note
# insert. Formula is function.insert(index #, new string)
hotel = ['bed', 'bags', 'bar', 'restaurant']
hotel.insert(1, 'garage')
print(f'{hotel}')

# Seeing the World

locations = ['himalaya', 'andes', 'tierra del fuego', 'labrador', 'guam']

print("Original order:")
print(locations)

print("\nAlphabetical:")
print(sorted(locations))

print("\nOriginal order:")
print(locations)

print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))

print("\nOriginal order:")
print(locations)

print("\nReversed:")
locations.reverse()
print(locations)

print("\nOriginal order:")
locations.reverse()
print(locations)

print("\nAlphabetical")
locations.sort()
print(locations)

print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)

# Loop is repetitve function. We us it to manipulate  list.
cars = ['bmw', 'audi', 'toyota', 'subaru']
for car in cars:
    print(f"{car.title()}, that is luxuruous vehicle.")

pizza_name_list = ['veggies', 'pepporoni', 'pineaple', 'mushroom']
for pizza in pizza_name_list:
  print(f"I like {pizza} pizza \n")

# Transform  range numbers into list
numbers = list (range(1,6))
print(numbers)

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team: \n")
for player in players[:3]:
    print(player.title())

# copy list by using [:]
my_foods = ['pizza', 'falafeel', 'carrot cake']
friends_foods = my_foods[:]

print("My favourite foods are: ")
print(my_foods)

print("\nMy friend's favourite foods are: ")
print(friends_foods)


# insert. Formula is function.insert(index #, new string)
hotel = ['bed', 'bags', 'bar', 'restaurant']
hotel.insert(1, 'garage')
print(f'{hotel}')

# Create a list and make a duplicate
pizza_name_list = ['veggies', 'pepporoni', 'pineaple', 'mushroom']

friend_pizzas = pizza_name_list[:]
friend_pizzas.append("avocado")
print(f"{friend_pizzas[1:3]}")

# Testing Multiple Conditions
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepporoni")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")











