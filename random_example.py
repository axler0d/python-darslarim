import random
m = int(input("mga qiymat kiriting: "))
n = int(input("nga qiymat kiriting: "))
if m > n:  
    print("m katta n dan")
    print("qiymatni boshqa kiriting!!!")
    #1break
a = random.randint(m, n)
print("Sirli son: ", a)
