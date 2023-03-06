# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# Input: 11 6
# Input: 2 4 6 8 10 12 10 8 6 4 2
# Input: 3 6 9 12 15 18

# Output: 6 12


length_list_1 = int(input('Введите длину 1-го словаря: '))
list_1 = list(int(input(f'{i+1} элемент 1-го словаря: ')) for i in range(length_list_1))

sort_list_1 = set(list_1)

for i in list_1:
    sort_list_1.add(i)

length_list_2 = int(input('Введите длину 2-го словаря: '))
list_2 = list(int(input(f'{i+1} элемент 2-го словаря: ')) for i in range(length_list_2))

sort_list_2 = set(list_2)

for i in list_2:
    sort_list_2.add(i)

output_list = list(sort_list_1 & sort_list_2)
output_list.sort()
print(output_list)

