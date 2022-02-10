import os

# TASK 1
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
                'ingredient_name': ing[0].strip(),
                'quantity': int(ing[1]),
                'measure': ing[2].strip()
            })

    return (name, ingredients)

# TASK 2
# Я видел, что в условии задачи функция принимает только два аргумента:
# список блюд и кол-во персон, но каким образом тогда можно узнать рецепты
# блюд изнутри функции, избегая использования глобальных переменных и сохраняя 'гибкость' 
# использования функции? Я посчитал, что лучше будет добавить третий аргумент: cook_book
def get_shop_list_by_dishes(cook_book, dishes, person_count):
    ings = [ing for dish in dishes for ing in cook_book[dish]]
    shop_list = {}
    for ing in ings:
        if ing['ingredient_name'] in shop_list:
            shop_list[ing['ingredient_name']]['quantity'] += ing['quantity'] * person_count
        else:
            shop_list[ing['ingredient_name']] = {
                    'quantity' : ing['quantity'] * person_count, 
                    'measure' : ing['measure']
                }

    return shop_list


cook_book = cook_book_from_file('recipes.txt')
print(get_shop_list_by_dishes(cook_book, ['Омлет', 'Фахитос'], 2))


