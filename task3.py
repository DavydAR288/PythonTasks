# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся.
# Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# import math
a = int(input("Enter the number of students in the first grade> "))
b = int(input("Enter the number of students in the second grade> "))
c = int(input("Enter the number of students in the third grade> "))
# class_tables_A=math.ceil(a/2)
# class_tables_B=math.ceil(b/2)
# class_tables_C=math.ceil(c/2)
class_tables_A = a // 2 + a % 2
class_tables_B = b // 2 + b % 2
class_tables_C = c // 2 + c % 2
# summ_tables=round(class_tables_A+class_tables_B+class_tables_C, 0)
summ_tables = class_tables_A + class_tables_B + class_tables_C
print("The smallest number of desks for all students> ", summ_tables)
