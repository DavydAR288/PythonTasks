def write_data(data):
    with open("telephone_book\db.txt", "a") as file:
        file.writelines(data)
        print("\nЗапись сделана\n")


def delete_data():
    with open("telephone_book\db.txt", "w") as file:
        print("\nВсе записи стерты\n")


def search_data(data_quest):
    with open("telephone_book\db.txt", "r") as file:
        file.seek(0)
        data = file.readlines()
        flag = False
        for i in data:
            if data_quest in i:
                print(i)
                flag = True
            else:
                flag == False
        if flag == True:
            print("Запись найдена\n")
        else:
            print("\nЗапись не найдена\n")


def sort_data():
    with open("telephone_book\db.txt", "r") as file:
        data = file.readlines()
        data.sort()
    with open("telephone_book\db.txt", "w") as file:
        file.writelines(data)
        print("\nСортировка сделана\n")


def view_families():
    with open("telephone_book\db.txt", "r") as file:
        data = file.readlines()
        for i in data:
            x = i.split("; ")
            print(x[1])
        print("\nФамилии выведены\n")


def view_all():
    with open("telephone_book\db.txt", "r") as file:
        data = file.readlines()
        c=1
        for i in data:
            print(c,": ",i.split("\n")[0])
            c+=1
        print("\nВсе записи выведены\n")

def delete(number):
    with open("telephone_book\db.txt", "r") as file:
        data = file.readlines()
        c=1
        correct=list()
        for i in data:
            if c!=number:
                correct.append(i)
            c+=1
    with open("telephone_book\db.txt", "w") as file:
        file.writelines(correct)
        print("\nЗапись удалена\n")

def correct(father):
    with open("telephone_book\db.txt", "r") as file:
        data = file.readlines()
        correct=list()
        flag=False
        for i in data:
            x=i.split("; ")
            if father == x[1]:
                flag=True
            else:
                correct.append(i)
    if flag==True:
        with open("telephone_book\db.txt", "w") as file:
            file.writelines(correct)
            return True
    else:
        print("\nЗапись не найдена\n")
        return False
