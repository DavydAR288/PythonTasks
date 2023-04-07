# Вагоны в электричке пронумерованы натуральными числами,
# начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»;
# это зависит от того, в какую сторону едет электричка).
# В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j.
# Он хочет определить, сколько всего вагонов в электричке.
# Напишите программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

wagon_number_account = int(input("Enter the number of the car in the account> "))  # i
wagon_number = int(
    input("Enter the number of the wagon that is indicated on it> ")
)  # j
if wagon_number_account == wagon_number:
    print(
        "Without additional information, it is impossible to determine the number of wagons"
    )
else:
    sum_wagons = wagon_number_account + wagon_number - 1
    print("The summ of wagons> ", sum_wagons)
