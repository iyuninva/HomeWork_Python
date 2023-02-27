# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 6 -> 5

ListLength = int(input("Длина списка: "))
print("Заполнение списка с клавиатуры: ")
list_1 = list(int(input(f"{[i+1]}: ")) for i in range(ListLength))
print(f"Создан список {list_1} с колличеством элементов: {len(list_1)}")
LookingNumber = int(input("Введите число: "))

MinNumber = 0

MinDifference = abs(LookingNumber - list_1[0])

for i in range(len(list_1)):
    if abs(LookingNumber - list_1[i]) < MinDifference:
        MinDifferenceNumber = abs(LookingNumber - list_1[i])
        MinNumber = list_1[i]

print(MinNumber)
