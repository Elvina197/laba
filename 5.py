#12 вариант
print("Введите 10 элементов массива А ")
A = []

for i in range(10):
    flag = False
    while not flag:
        s = input(f" A[{i}]: ")
        if s.isdigit():
            A.append(int(s))
            flag = True
        else:
            print("Ошибка. Введите целое число")
B = []

for i in range(10):
    flag = False
    while not flag:
        s = input(f" B[{i}]: ")
        if s.isdigit():
            B.append(int(s))
            flag = True
        else:
            print("Ошибка. Введите целое число")

for i in range(10):
    A[i], B[i] = B[i], A[i]

print(f"\nПреобразованный массив А: ")
for x in A:
    print(x, end=" ")
print()

print(f"\nПреобразованный массив B: ")
for x in B:
    print(x, end=" ")
print()

