class Talaba:
    def __init__(self,ism,yosh):
        self.ism = ism
        self.yosh =  yosh
        
    @property
    def yosh(self):
        return self.__yosh
    
    @yosh.setter
    def yosh(self,yangi):
        if 0<yangi<120:
            self.__yosh = yangi
        else:
            raise ValueError("QIymat kiritishda xatolik bor: ")
    def __str__(self):
        return f"{self.ism} {self.yosh}"
while True:
    try:
        ism = input("Ismingizni kiriting: ")
        yosh = int(input("Yoshingizni kiriting: "))
        talaba = Talaba(ism,yosh)
        print(talaba)
        break
    except ValueError as xato:
        print("Xato:",xato)
    