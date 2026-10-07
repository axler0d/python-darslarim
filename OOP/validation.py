class Talaba:
    def __init__(self,ism,yosh):
        self.ism = ism
        self.yosh =  yosh

    @property
    def ism(self):
        return self.__ism

    @ism.setter
    def ism(self,yangi):
        if yangi.isalpha():
            self.__ism = yangi
        else:
            raise ValueError("Ism xato kiritilgan")
    @property
    def yosh(self):
        return self.__yosh
    
    @yosh.setter
    def yosh(self,yangi):
        if 0<yangi<120:
            self.__yosh = yangi
        else:
            raise ValueError("Qiymat chegarada emas!!!")
    def __str__(self):
        return f"{self.ism.title()} {self.yosh}"

while True:
    try:
        ism = input("Ismingizni kiriting: ")
        talaba = Talaba(ism,1)
        break
    except ValueError as xato:
        print(xato)
while True:
    matn = input("yoshingizni kiriting: ")
    try:
        yosh = int(matn)
    except ValueError:
        print("Yosh raqamlardan iborat bo'lsin!!!")
        continue

    try:
        talaba = Talaba(ism,yosh)
        break
    except ValueError as xato:
        print(xato)
print(talaba)
