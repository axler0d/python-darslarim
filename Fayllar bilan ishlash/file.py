with open("file.txt","a") as fayl:
    fayl.write("Assalomu alekum qondaysan\n")
with open("file.txt","r") as fayl:
    mazmun = fayl.read()
    print(mazmun)

with open("Tarjimaihol.txt","a") as fayl:
    fayl.write("Salom mening ismim Bekmirza, yoshim 23 da\n")
with open("Tarjimaihol.txt","r") as fayl:
    mazmun = fayl.read()
    print(mazmun)
ism = input("Ismingizni kiriting: ")
with open("Tarjimaihol.txt","a", encoding="utf-8") as fayl:
    fayl.write(ism + "\n")
with open("Tarjimaihol.txt", "r", encoding="utf-8") as fayl:
    for soz in fayl:
        print(soz.strip())