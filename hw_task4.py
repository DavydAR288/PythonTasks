#  Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
# Ввести проверку на кратность 6

s = int(input())
# x + x + 4x = s > 6x = s > x = s/6
if s % 6 == 0:
    x = int(s/6)
    print(x, 4*x, x)
else:
    print("Error input")
