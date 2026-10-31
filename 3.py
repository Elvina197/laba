#12 вариант
text = input("Введите строку: ")
w = text.split()

flag = False
for i in w:
    clovo = i.strip(".,!?;:-\"'()[]{}")
    if len(clovo) > 0 and clovo[-1] == 'я':
        print(clovo)
        flag = True
if not flag:
    print("Слов не найдено")