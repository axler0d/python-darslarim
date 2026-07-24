class Talaba:
    def __init__(self,ism,familiya,yosh=0):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
    def __repr__(self):
        return f"{self.ism} {self.familiya} {self.yosh} yoshda"
talaba1 = Talaba("Bekmirza","Madaminov",24)
talaba2 = Talaba("Sardor","Muxtorov",17)
talabalar = [talaba1,talaba2]
print("Talabalar ro'yxati...")
for i in talabalar:
    print([i])