#12 вариант
flag = False
while not flag:
    n = input("Введите количество элементов списка: ")
    if n.isdigit() and int(n) > 0:
        n = int(n)
        flag = True
    else:
        print("Ошибка. Введите целое положительное число")

sp = []
for i in range(n):
    flag = False
    while not flag:
        x = input(f" Элемент {i + 1}: ")
        if x.isdigit():
            sp.append(int(x))
            flag = True
        else:
            print("Ошибка. Введите целое число")

mi = 10**10
flag = False
for x in sp:
    if x % 2 != 0:
        if not flag or x < mi:
            mi = x
            flag = True
if flag:
    print(f"Наименьший нечетный элемент: {mi}")
else:
    print("В списке нет нечетный элементов")