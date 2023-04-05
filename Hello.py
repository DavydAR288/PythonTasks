n=0
i=0
c=0
while (c==0):
    n=int(input("Input number type of integer (1-5): "))
    if (n>0 and n<6): c=1
    else: print("Incorrect input! Try again!")
nr=range(n)
for i in nr:
    print(i+1,"> Hello, world!")