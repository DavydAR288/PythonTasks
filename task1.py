# За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

# n=int(input("How many kilometers does the car pass for a day?> "))
# m=int(input("Enter the route that you need to drive> "))
# d=int(m/n)
# print("To drive the route is necessary ",d," days")

import math

distance = int(input("Enter the distance to which you need to drive "))
max_distance_one_car = int(input("Enter the maximum distance by 1 car "))
num_car = math.ceil(max_distance_one_car / distance)
print("Required ", num_car, " days")

# (m+n-1//n) - окргуление в большую сторону без использования библиотеки
# (m//n + int(m%n!=0)) - логическое выражение преобразуем в int
