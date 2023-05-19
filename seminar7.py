#lambda, filter, map, zip, enumerate, list comprehension

#list comprehension
# a = [i if i < 3 else 0 for i in range(5)]
# print(a)
# for i in range(6):
#     a.append(5)
# print(a)

#enumerate
# a = [0, 1, 2, 3, 2, 5, 1]
# for indx,val in enumerate(a):
#     print(indx,val)

#zip
# a = (1,2,4,5,6)
# b = "abcd"
# f = {45:"b",54:"c",87:"fr"}
# for i1,i2,i3 in zip(a,b,f.values()):
#     print(i1,i2,i3)

#lambda
# def summa(a,b):
#     return a+b
a = lambda x,y: x+y if x == 3 else 0
print(a(3,4))

#map
# a = [1,2,3,4,5,6]
# a = list(map(lambda el: el if el%2==0 else 0,a))
# print(a)

#filter
# a = [1, 2, 3, 4, 5, 6]
# a = list(filter(lambda el: True if el%2==0 else False,a))
# print(a)