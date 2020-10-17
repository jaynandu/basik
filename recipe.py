box = 'stuff'

ingredients = ['apples', 'sugar']

order = ['flour', 'eggs', 'milk']

ingredients = ingredients + order

print(ingredients)

# functions


def recipe(ingredients):
    for item in ingredients:
        print(f"Add {item} to mix")

    print("Put mix into the oven")


recipe(ingredients)
