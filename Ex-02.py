# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

Number = int(input("Введите трехзначное число: "))
CheckStr = str(Number)

if len(CheckStr) == 3:
    sum = 0
    sum = Number // 100 + Number // 10 % 10 + Number % 10
    print(sum)
else:
    print("Error: Введите трехзначное число!")

