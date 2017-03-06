import sys

# cook_book = {
#     'scrumble_egg_tomato': [
#         {'ingridient_name': 'eggs', 'quant': 2, 'measure': 'piece'},
#         {'ingridient_name': 'tomato', 'quant': 100, 'measure': 'gr.'}
#     ],
#     'steak': [
#         {'ingridient_name': 'meat', 'quant': 300, 'measure': 'gr.'},
#         {'ingridient_name': 'spices', 'quant': 5, 'measure': 'gr.'},
#         {'ingridient_name': 'olive_oil', 'quant': 100, 'measure': 'ml.'}
#     ],
#     'salad': [
#         {'ingridient_name': 'tomato', 'quant': 100, 'measure': 'gr.'},
#         {'ingridient_name': 'cucamber', 'quant': 100, 'measure': 'gr.'},
#         {'ingridient_name': 'olive_oil', 'quant': 100, 'measure': 'ml.'},
#         {'ingridient_name': 'onion', 'quant': 1, 'measure': 'piece'}
#     ]
# }


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quant'] *= person_count
            # print(new_shop_list_item)
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quant'] += new_shop_list_item['quant']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{ingridient_name} {quant} {measure}'.format(**shop_list_item))


def create_shop_list(cook_book):
    person_count = int(input('input quant person: '))
    dishes = input('input meal by one person per column: ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)
    print_shop_list(shop_list)


def read_cook_book_from_file(cook_book_file_name):
    cook_book = dict()

    with open(cook_book_file_name) as file:
        read_key = True
        read_ing_number = False
        read_ing = 0
        last_key = None

        for l in file:
            if not l:
                continue
            l = l.strip()
            if read_key:
                cook_book[l] = []
                last_key = l
                read_key = False
                read_ing_number = True
            elif read_ing_number:
                read_ing = int(l)
                read_ing_number = False
            else:
                name, qty, unit = l.split("|")
                cook_book[last_key].append({
                    'ingridient_name': name.strip(),
                    'quant': qty.strip(),
                    'measure': unit.strip()
                })
                read_ing -= 1
                if read_ing <= 0:
                    read_key = True
                    read_ing_number = False

    return cook_book


if __name__ == '__main__':
    cook_book_file_name = sys.argv[1]
    cook_book = read_cook_book_from_file(cook_book_file_name)
    create_shop_list(cook_book)