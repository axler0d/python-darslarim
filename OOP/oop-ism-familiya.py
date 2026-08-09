class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
    def get_info(self):
        return f"{self.ism} {self.familiya} {self.tyil}da tug'ilgan va {self.bosqich}-bosqich talabasi"
    def set_bosqich(self,bosqich):
        self.bosqich = bosqich
    def update_bosqich(self):
        """Talabanining bosqichini 1taga ko'paytirish"""
        self.bosqich += 1
talaba1 = Talaba("Bekmirza","Madaminov",2003)
#talaba1.tanishtir()
talaba1.set_bosqich(5)
print(talaba1.get_info())
talaba1.update_bosqich()
print(talaba1.bosqich)
