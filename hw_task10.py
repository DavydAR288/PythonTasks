# Задача 10:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

n = int(input("N = "))
coinsE = 0
coinsT = 0
status = 0
for i in range(n):
    check = 1
    while check == 1:
        print("Input status coin", i+1, " = (0, 1)")
        d = int(input())
        if -1 < d < 2:
            check = 0
    if d == 0:
        coinsE += 1
    else:
        coinsT += 1
if coinsE > coinsT:
    status = coinsT
elif coinsE == coinsT:
    status = coinsT
else:
    status = coinsE
print("Turn the coins ->", status)
