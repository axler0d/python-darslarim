print("Kalkulyatorga xush kelibsiz")

print("Amallardan birini tanlang (1-2-3-4)")
print("""
      1. Qo'shish
      2. ayirish        
      3. Ko'paytirish
      4.bo'lish
      """)

a = float(input("Birinchi sonni kiriting:"))
b = float((input("Ikkinchi sonni kiriting:")))

amal = int((input("Amalni yozing( 1 / 2 / 3 / 4 ):")))

if amal == 1:
    print("natija:",a+b)
elif amal == 2:
    print("natija",a-b)
elif amal == 3:
    print("natija",a*b)
elif amal == 4:
    if b != 0:
        print("natija",a/b)
    else:
        print("Kechirasiz, ikkinchi son 0 ga teng bo'lmaslik kerak")

