def user_input():
    ask = int(input("Выбери ниже:\n 0 - Стереть все записи\n 1 - Добавить запись\n"
                    " 2 - Найти запись\n 3 - Сортировать\n"
                    " 4 - Вывести только фамилии\n 5 - Вывести все записи\n"
                    " 6 - Изменить строку\n 7 - Удалить строку\n 8 - Выход\n > "))
    return ask


def input_data():
    name = input("Введите имя > ")
    family = input("Введите фамилию > ")
    father = input("Введите отчетство > ")
    bdate = input("Введите дату рождения > ")
    phone = input("Введите телефон > ")
    ask = name+"; "+family+"; "+father+"; "+bdate+"; "+phone+"; "+"\n"
    return ask


def input_search():
    ask = (input("Введите строку поиска > "))
    return ask

def input_delete():
    ask = int(input("Введите строку для удаления > "))
    return ask

def input_correct():
    ask = (input("Введите фамилию для изменения данных > "))
    return ask