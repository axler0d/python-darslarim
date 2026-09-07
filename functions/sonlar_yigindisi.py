def eng_katta_son(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
a = int(input("Son kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
c = int(input("Uchinchi sonni kiriting: "))
natija = eng_katta_son (a, b, c)
print("Natija: ", natija)

def juft_toq_son(a):
    if a % 2 == 0:
        return "Juft son"
    else:
        return "Toq son"
a = int(input("Son kiriting: "))
natija = juft_toq_son(a)
print("Natija: ", natija)