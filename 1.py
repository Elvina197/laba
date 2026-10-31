#12 вариант
flag = False
while not flag:
    n = input("Введите количество учеников в каждом классе ")
    if n.isdigit() and int(n) > 0:
        n = int(n)
        flag = True
    else:
        print('Ошибка. Введите целое положительное число')

sum1 = 0
print("Введите оценки учеников 1 класса: ")
for i in range(n):
    flag = False
    while not flag:
        s = input(f" Ученик {i + 1}: ")
        if s.isdigit() and 1 <= int(s) <= 5:
            sum1 += int(s)
            flag = True
        else:
            print("Ошибка. Введите цифру от 1 до 5")
sum2 = 0
print("Введите оценки учеников 2 класса: ")
for i in range(n):
    flag = False
    while not flag:
        s = input(f" Ученик {i + 1}: ")
        if s.isdigit() and 1 <= int(s) <= 5:
            sum2 += int(s)
            flag = True
        else:
            print("Ошибка. Введите цифру от 1 до 5")


print(f"\nСредняя оценка в 1 классе: {sum1 / n:.2f}")
print(f"\nСредняя оценка в 2 классе: {sum2 / n:.2f}")