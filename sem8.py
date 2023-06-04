with open("sem8.txt", "w") as file:
    a = ["asd\n", "dfg\n", "qwe\n", "ert\n"]
    file.writelines(a)  # запись строк
    file.write("aaa")  # запись строки

with open("sem8.txt", "r") as file:
    for i in range(3):
        # strip убирает лишний перенос строки в файле
        print(file.readline().strip())
    # перенос позиции чтения/записи на указанную позицию
    file.seek(0)
    print(file.read())
    # читает файл в виде списка / парсинг файла
    file.seek(0)
    lst = file.readlines()
    print(lst)

a = [(1, 3, 6), (2, 1, 7), (0, 6, 9)]
# сортирует список кортежей по 2-му элементу кортежейб работает со строками. По 1-му символу сравнивемт при равенсте 2-го символа
a.sort(key=lambda x: (x[1], x[0]))
# функция sorted отличается от метода sort тем, что создает новый список, выделяя доп память
b = sorted(a, key=lambda x: (x[0], x[1], x[2]))
print(a)
print(b)
# ищем кортеж с максимальной суммой
print(max(a, key=lambda x: x[0]+x[1]+x[2]))
