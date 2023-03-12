# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]
#   9  10  8  10  7

import random

first_number_range = int(input('Введите начало диапазона: '))
second_number_range = int(input('Введите конец диапазона: '))

list_1 = list(int(random.randint(-10, 10)) for i in range(20))

print('Полученный список:')
print(list_1)

list_result = {}


for i in range(len(list_1)):
    if list_1[i] >= first_number_range and list_1[i] <= second_number_range:
        list_result[f'Индекс - {i}'] = str(f'Значение - {list_1[i]}')

print('Результат:')
for key, value in list_result.items():
    print('{}: {}'.format(key,value))
