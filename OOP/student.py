class Talaba:
    def __init__(self,ism,yosh,instut,baho):
        self.ism = ism
        self.yosh = yosh
        self.instut = instut
        self.baho = baho
    def malumot(self):
        return f"Ismi {self.ism}, yoshi {self.yosh}, universiteti {self.instut}"
    def yil_top(self):
        return 2026 - self.yosh
    def holat(self):
        if self.yosh>18:
            print("voyaga yetgan")
        else:
            print("voyaga yetmagan")
    def ball(self):
        if self.baho>60:
            print("Talaba imtihondan o'tdi")
        else:
            print("Talaba imtihondan o'ta olmadi")
    def institutni_ozgartir(self, yangi_institut):
        self.instut = yangi_institut
ism = input("Ismingizni kiriting: ")
yosh = int(input("Yoshingizni kiriting: "))
instut = input("Instutingizni kiriting: ")
baho = int(input("Talaba bahosini kiriting: "))
talaba1 = Talaba(ism,yosh,instut,baho)
natija1 = talaba1.yil_top()
natija = talaba1.malumot()
talaba1.holat()
talaba1.ball()
talaba1.institutni_ozgartir("INHA")
print("Talaba",natija1,'yili tugilgan')
print(natija)

class Kitob():
    def __init__(self,nom,muallif,yil):
        self.muallif = muallif
        self.nom = nom 
        self.yil = yil 
kitob = Kitob("O'tkan kunlar",'O\'tkir Hoshimov',1995)
print(kitob.muallif)
