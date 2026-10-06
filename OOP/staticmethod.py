class Supper:

    def __init__(self,ism,yosh,baho):
        self.ism = ism
        self.yosh = yosh
        self.baho = baho

    @staticmethod
    def yosh_tek(yosh):
        if 0<yosh<120:
            print("Yosh to'g'ri kiritilgan!!!")
        else:
            print("Yosh noto'g'ri!!!")
    
    @staticmethod
    def kvadrat(son):
        return son**2

    @staticmethod
    def juftsonlar(sonlar):
        numbers = []
        for son in sonlar:
            if son % 2 == 0:
                numbers.append(son)
        return numbers
    @staticmethod
    def katta(sonlar):
        maks = 0
        for son in sonlar:
            if maks<son:
                maks = son
        return maks
    @staticmethod
    def parol(matn):
        if len(matn)>=8:
            print("Parol qabul qilindi")
        else:
            print("Parol yaroqsiz yoki kuchsiz")



ism = (input("Ismingizni kiriting: "))
yosh = int(input("yoshingizni kiriting: "))
baho = int(input("Baho: "))
talaba = Supper(ism,yosh,baho)
talaba.yosh_tek(yosh)   
sonlar = [2,3,4,5,6,7]
numbers = Supper.juftsonlar(sonlar)
print(numbers)

maks = Supper.katta(sonlar)
print("Katta son: ",maks)

parol = input("Parol: ")
Supper.parol(parol)