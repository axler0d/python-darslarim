class Xodim:

    chegara = 120

    def __init__(self,ism,yosh):
        self.ism = ism
        self.yosh = yosh

    def get_info(self):
        return f"{self.ism.title()} xodim yoshi {self.yosh}"
    
    @classmethod
    def yosh_tekshir(cls, yosh):
        while True:
            if 0 < yosh < cls.chegara:
                print(f"Yoshingiz to'g'ri")
                return yosh
            else:
                print("yoshni xato kiritdingiz!!!")
                yosh = int(input("Yoshni qayta kiriting: "))
            cls.yosh = yosh
class Dasturchi(Xodim):
    chegara = 60

    def __init__(self, ism, yosh,soha):
        super().__init__(ism, yosh)
        self.soha = soha

    def get_info(self):
        return super().get_info()+f" sohasi {self.soha}"

    @classmethod
    def yosh_tekshir(cls, yosh):
        return super().yosh_tekshir(yosh)
    
ism = input("Ismingizni kiriting: ")
yosh = int(input("Yoshingizni kiriting: "))
soha = input("Sohangiz: ")
yosh = Dasturchi.yosh_tekshir(yosh)
xodim = Dasturchi(ism,yosh,soha)
natija = xodim.get_info()
print(natija)