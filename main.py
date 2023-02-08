'''
Дано:

dct = {'person': {'in_dict': [1, 2, 3],
'after_list': {4, '5'},
'after_set': ('hello', )}}

Реалізувати спосіб, при якому кожен елемент даного словника (ключ та значення) стане ключем в іншому словнику.
Якщо в якості значення виступає послідовність (список), значить- кожен елемент списку стає ключем + сам список
також стає ключем (для цього перетворюємо його на кортеж).

Пам’ятаємо: цикл може містити в собі вкладений цикл. Сам функціонал орієнтований тільки на цей словник.
'''

dct = {'person': {'in_dict': [1, 2, 3],
                  'after_list': {4, '5'},
                  'after_set': ('hello', )}}
dct_new = {}
for value in dct.values():
    for key_value, value1 in zip(value.keys(), value.values()):
            for element in value1:
                if type(value1) == list or set:
                    t = tuple(value1)
                dct_new[key_value] = 1
                dct_new[t] = 2
                dct_new[element] = 3
print(f'dct_new: {dct_new}')