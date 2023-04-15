# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.
# Input:     5
# Output:  6
# while 0 1 1 2 3 5 8 13 A=n
#       1 2 3 4 5 6 7 8  i

n = int(input("A = "))
a1 = 1
a2 = 1
a = 1
i = 3
if n == 0:
    print("i = 1")
elif n == 1:
    print("i = 2, 3")
elif n < 0:
    print("Error input")
else:
    while a < n:
        i += 1
        a = a1+a2
        a1 = a2
        a2 = a
    if n == a:
        print("i =", i)
    else:
        print("-1")
