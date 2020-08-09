# Looking for name in dict
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for name in favorite_languages.keys():
    print(name.title())

# A list  in a dictionary

# Store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# Summarize the order
print(f"You ordered a {pizza ['crust']} - crust pizza"
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

