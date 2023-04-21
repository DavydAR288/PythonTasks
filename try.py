# Проверка на ошибки

a = "rt"
try:
    a = int(a)
except ValueError:
    print(1)