# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while
# Input:       5
# Output:    120
# while

n = int(input())
i = 1
f = 1
if n == 0:
    print("0! = 1")
elif n < 0:
    print("Error input")
else:
    while i<n+1:
        f*=i
        i+=1
print (f)