with open("fayl.txt", "w") as fayl:
    fayl.write("manti - 10 000 so'm\n")
    fayl.write("Osh - 25 000 so'm\n")
    fayl.write("Somsa - 6 000 so'm\n")

with open("fayl.txt", "r") as fayl:
    for qator in fayl:
        print(qator.strip())
with open("fayl.txt", "a") as fayl:
    fayl.write("Menyuga qo'shish kerak bo'lgan mahsulotlar>>>\n")
with open("fayl.txt","r") as fayl:
    mazmun = fayl.read()
    print(mazmun)

