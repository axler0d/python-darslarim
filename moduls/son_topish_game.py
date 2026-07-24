import random

while True:

    sirli_son = random.randint(1, 10)

    try:
        taxmin = int(input("1 dan 10 gacha son kiriting: "))
    except ValueError:
        print("Xato! Faqat son kiriting.")
        continue

    if taxmin == sirli_son:
        print("Tabriklayman! To'g'ri topdingiz.")
    else:
        print(f"Noto'g'ri. Sirli son {sirli_son} edi.")

    javob = input("Yana urinib ko'rmoqchimisiz? (ha/yo'q): ")

    if javob.lower() == "yo'q":
        print("O'yin tugadi. Rahmat o'ynaganingiz uchun!")
        break