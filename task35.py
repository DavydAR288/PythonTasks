# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)
# Input: 5
# Output: yes

 
def Prime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

print(Prime(5))

