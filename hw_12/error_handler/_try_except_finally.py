# 7. Створити конструкції try-except-finally


def pizza_ingredients(user_ingredients):
    user_in = []

    for ingredient in user_ingredients.split():
        if ingredient not in ingredients:
            raise Exception(
                f"Please, choose ingredients from the list: {ingredients}")

        user_in.append(ingredient)

    return user_in


ingredients = ["tomato", "cheese", "olive", "prosciutto", "pear", "honey"]

user_ingredients = input(
    f"Choose ingredients from the list to add in your pizza: {ingredients}: ")

user_ingredients = user_ingredients.replace(',', ' ')
user_ingredients_list = user_ingredients.split()

try:
    user_in = pizza_ingredients(user_ingredients)
    print(f"Selected ingredients: {user_in}")

    if len(user_in) <= 3:
        print("Total price: 20 cad")
    elif len(user_in) >= 4:
        print("Total price: 40 cad")

except Exception as e:
    print(f"Error: {e}")

finally:
    print("Thank you for your order!")
