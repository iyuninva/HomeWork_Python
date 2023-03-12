# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

list_number = list(int(i) for i in input('Введите 1-начало отсчета, 2-шаг, 3-сколько чисел: ').split())

list_progression = list()

first_number = list_number[0]
difference = list_number[1]
quantity = list_number[2]
next_number = 0 

for i in range(quantity):
    next_number = first_number + i * difference
    list_progression.append(next_number)

print(list_progression)