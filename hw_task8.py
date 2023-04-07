#  Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input())
m = int(input())
k = int(input())
if k >= n or k >= m:
    if k%n==0 and k//n<=m:
        print("Yes")
    elif k%m==0 and k//m<=n:
        print("Yes")
    else:
        print("No")
else:
    print("No")


# O O O
# O O O
# 3, 2
# 4