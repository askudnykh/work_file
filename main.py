

with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dishes_name = line.strip()
        ingredient_count = int(file.readline())
        detail = []
        for _ in range(ingredient_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            detail.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
        file.readline()
        cook_book[dishes_name] = detail
    print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            detail_list = cook_book[dish]
            for ingr in detail_list:
                if ingr['ingredient_name'] in result:
                    result[ingr['ingredient_name']]['quantity'] += ingr['quantity'] * person_count
                else:
                    result[ingr['ingredient_name']] = {'measure': ingr['measure'], 'quantity': ingr['quantity'] * person_count}
    print(result)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

f = open('file_union.txt', 'w', encoding='utf-8')
dict_file_len = {}
dict_file_content = {}
with open('1.txt', encoding='utf-8') as file1:
    file_content = file1.readlines()
    file1.seek(0)
    len_ = len(file1.readlines())
    dict_file_len[file1.name] = len_
    dict_file_content[file1.name] = file_content

with open('2.txt', encoding='utf-8') as file1:
    file_content = file1.readlines()
    file1.seek(0)
    len_ = len(file1.readlines())
    dict_file_len[file1.name] = len_
    dict_file_content[file1.name] = file_content

with open('3.txt', encoding='utf-8') as file1:
    file_content = file1.readlines()
    file1.seek(0)
    len_ = len(file1.readlines())
    dict_file_len[file1.name] = len_
    dict_file_content[file1.name] = file_content

sorted_dict = dict(sorted(dict_file_len.items(), key=lambda item: item[1]))

for file in sorted_dict:
    f.write('\n'+file+'\n')
    f.write(str(sorted_dict[file])+'\n')
    for line1 in dict_file_content[file]:
        f.write(line1)

print(dict_file_len)
print(dict_file_content)
print(sorted_dict)
f.close()
