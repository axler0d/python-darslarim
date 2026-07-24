class Transport:
    def yur(self):
        print("Transport harakatlanmoqda")
class Mashina(Transport):
    def yur(self):
        print("Mashina yo'lda harakatlanmoqda")    
m = Mashina()
m.yur()





#class Hayvon:
#    def ovqatlan(self):
#        print("ovqatlanmoqda")
#class Mushuk(Hayvon):
#    pass
#M = Mushuk()
#M.ovqatlan()

#class Inson:
#    def __init__(self,ism,yosh):
#        self.ism = ism
#        self.yosh = yosh
#        print(f"{self.ism} {self.yosh}")
#class Talaba(Inson):
#    def __init__(self, ism, yosh):
#        super().__init__(ism, yosh) 

#m = Talaba("Alisher",56)

