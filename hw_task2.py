#  Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

s = 0
n = int(input())
if n > 99 and n < 1000:
    for i in range(3):
        s = s + n % 10
        n = n//10
    print(s)
else:
    print("Error input")
