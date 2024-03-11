def create_cookbook():
    with open('data.txt', encoding='utf-8') as file:
        results = []
        recipe = []
        for line in file.readlines():
            if line.strip():
                recipe.append(line.strip())
            else:
                results.append(recipe)
                recipe = []

    data = {}
    for recipe in results:
        data[recipe[0]] = []
        for ingredient in recipe[2: 2 + int(recipe[1])]:
            info_ingredient = ingredient.split(' | ')
            data[recipe[0]].append({
                'ingredient_name': info_ingredient[0],
                'quantity': info_ingredient[1],
                'measure': info_ingredient[2],
            })
    return data


def get_shop_list_by_dishes(dishes, person):
    recipes = create_cookbook()
    result = {}
    for recipe, ingredients in recipes.items():
        if recipe in dishes:
            for ingredient in ingredients:
                name = ingredient["name"]
                quantity = int(ingredient["quantity"]) * person
                pieces = ingredient["pieces"]
                if name not in result.keys():
                    result[name] = {
                        "pieces": pieces,
                        "quantity": quantity
                    }
                else:
                    result[name]["quantity"] += quantity
    return result
