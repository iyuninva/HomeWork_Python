# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

QuantityNumber = int(input("Колличество монеток: "))
One = 0
Zero = 0
count = 0

while count < QuantityNumber:
    i = int(input(f"Орел(1) Решка(0): {count+1} монета: "))
    if i == 1:
        One += 1
        count += 1
    elif i == 0:
        Zero += 1
        count += 1

if One >= Zero:
    print("Нужно перевернуть:", Zero)
else:
    print("Нужно перевернуть:", One)