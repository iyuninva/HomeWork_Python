# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

Number = int(input("Введите число: "))

count = 0
while 2 ** count <= Number:
    print(f"2^{count} = {2**count}")
    count += 1
    
