print("Kalkulyator dasturiga xush kelibsiz!")
#print("Iltimos, quyidagi amallardan birini tanlang:")
print("1. Qo'shish")
print("2. Ayirish")
print("3. Ko'paytirish")
print("4. Bo'lish")
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
amal = int(input("Amalni tanlang (1-4): "))

if amal == 1:
    print(f"Natija: {a + b}")
elif amal == 2:
    print(f"Natija: {a - b}")
elif amal == 3:
    print(f"Natija: {a * b}")
elif amal == 4:
    if b != 0:
        print(f"Natija: {a / b}")
    else:
        print("Iltimos, ikkinchi sonni 0 ga teng bo'lmasdan kiriting.")
