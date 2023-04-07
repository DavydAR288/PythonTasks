# Пользователь вводит целое число.
# Выведите его строку-описание вида "отрицательное четное число", "нулевое число", "положительное нечетное число",
# например, численным описанием числа 190 является строка "положительное четное число".

number = int(input("Enter number> "))

if number > 0 and number % 2 == 0:
    print("Number is positive even")
elif number > 0 and number % 2 != 0:
    print("Number is positive odd")
elif number < 0 and number % 2 == 0:
    print("Number is negative even")
elif number < 0 and number % 2 != 0:
    print("Number is negative odd")
else:
    print("Number is null")
