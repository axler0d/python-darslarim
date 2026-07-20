kontaktlar = {}
while True:
    amal = int(input("""Bajarmoqchi bo'lgan amalingizni tanlang"
    1. Kontakt qo'shish
    2. Kontaktni qidirish
    3. Barcha kontaktlarni chiqarish
    4. Chiqish
    >>>      """))
    if amal == 1:
        while True:
            ism = input("Ismni kiriting: ")
            raqam = int(input("Raqamni kiriting: "))

            kontaktlar[ism] = raqam
    
            javob = input("Yana kontakt kiritasizmi? ")
            if javob.lower() not in ['ha','da','+','yes']:
                break
    if amal == 3:
        for kalit,qiymat in kontaktlar.items():
            print(f"{kalit.capitalize()} : {qiymat}")
    
    if amal == 2:
        name = input("Qidirmoqchi bo'lgan ismni kiriting: ")

        if name in kontaktlar:
            print("Topildi")
            print(f"{name}: {kontaktlar[name]}")
        else:
            print("Bunday kontakt topilmadi.")
    if amal == 4:
        print("Dastur tugadi.")
        break
   