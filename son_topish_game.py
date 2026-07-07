import random

while True:

    sirli_son = random.randint(1, 10)

    taxmin =int(input("1 dan 10 gacha son kiriting: "))
    if type(taxmin) == 'string':
        print('Raqam kiriting!!!')
        break

    if taxmin == sirli_son:
        print("Tabriklayman! To'g'ri topdingiz.")
    else:
        print(f"Noto'g'ri. Sirli son {sirli_son} edi.")

    javob = input("Yana urinib ko'rmoqchimisiz? (ha/yo'q): ")
    if javob.lower() == "yo'q":
        print("O'yin tugadi. Rahmat o'ynaganingiz uchun!")
        break