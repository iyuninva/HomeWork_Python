# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.


NumberSum = int(input("Введите сумму чисел X И Y: "))
NumberСom = int(input("Введите произведение чисел X И Y: "))

FlagStop = True

for i in range(NumberSum):
    if FlagStop == False:
        break
    for j in range(NumberСom):
        if i + j == NumberSum and i * j == NumberСom:
                print(f"Число X = {i}, а число Y = {j}")
                FlagStop = False
                

