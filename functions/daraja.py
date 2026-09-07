def summa(a,b):
    s=0
    for i in range(a,b+1):
        s=s+i
    return s
a = int(input("a ga qiymat kiriting: "))
b = int(input("darajani kiriting: "))
c = summa(a,b)
print("Daraja: ",c)
