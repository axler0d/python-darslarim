import random
def son_topish(x=10):
    tasodifiy_son = random.randint(1, x)
    print(f"Men 1 dan 10 gacha son o'yladim. Topishga harakat qiling!")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input("Sizning taxminingiz: "))
        if taxmin>tasodifiy_son:
            print("Sizning taxminingiz katta. Qayta urinib ko'ring.")
        elif taxmin<tasodifiy_son:
            print("Sizning taxminingiz kichik. Qayta urinib ko'ring.")
        else:
            print(f"Tabriklayman! Siz yutdingiz")
            break
    print(f"Siz {taxminlar} ta taxmin bilan topdingiz.")
    return taxminlar

def son_top_pc(x=10):
    print(f"1 dan {x} gacha son o'ylang. Men topishga harakat qilaman!")
    pastki_chegara = 1
    yuqori_chegara = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if pastki_chegara != yuqori_chegara:
            taxmin = random.randint(pastki_chegara, yuqori_chegara)
        else:
            taxmin = pastki_chegara
        
        javob = input(f"Siz {taxmin} sonini o'yladingiz: (-) kichik, (+) katta, (t) to'g'ri: ").lower()

        if javob == "-":
            yuqori_chegara = taxmin - 1
        elif javob == "+":
            pastki_chegara = taxmin + 1 
        else:
            break
       
       
    print(f"Men {taxminlar} ta taxmin bilan topdim.")
    return taxminlar

def play(x=10):
    yana = True
    while yana:
        taxminlar_foydalanuvchi = son_topish(x)
        taxminlar_pc = son_top_pc(x)

        if taxminlar_foydalanuvchi < taxminlar_pc:
            print("Siz yutdingiz!")
        elif taxminlar_foydalanuvchi > taxminlar_pc:
            print("Men yutdim!")
        else:
            print("Durrang!")
        
play()
javob = input("Yana o'ynaysizmi? (ha/yo'q): ").lower()

if javob != "ha":
    yana = False