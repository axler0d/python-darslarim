def hisobla(a, b, amal):
    if amal == 1:
        return a + b
    elif amal == 2:
        return a - b
    elif amal == 3:
        return a * b
    elif amal == 4:
        if b == 0:
            return "0 ga bo‘lish mumkin emas"
        return a / b


a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))

while True:
    amal = int(input("Amalni tanlang (1:+, 2:-, 3:*, 4:/): "))

    if amal >= 1 and amal <= 4:
        break

    print("Noto‘g‘ri amal! 1 dan 4 gacha tanlang.")


natija = hisobla(a, b, amal)

print("Natija:", natija)