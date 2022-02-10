import os

def cook_book_from_file(path):
    with open(path, 'r') as f:
        raw = f.read().strip()

    recipes_raw = raw.split('\n\n')

    cook_book = {}
    for r in recipes_raw:
        name, ingredients = parse_recipe(r)
        cook_book[name] = ingredients

    return cook_book
            

def parse_recipe(r):
    recipe = r.strip().split("\n")
    name = recipe[0]

    recipe = recipe[2:]
    ingredients = []
    for ing in recipe:
        ing = ing.split("|")
        ingredients.append({
                'ingredient_name': ing[0],
                'quantity': int(ing[1]),
                'measure': ing[2]
            })

    return (name, ingredients)

# cook_book = cook_book_from_file('recipes.txt')
