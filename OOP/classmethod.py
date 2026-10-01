class Xodim:
    universitet = "TATU"
    def __init__(self,ism,yosh):
        self.ism = ism
        self.yosh = yosh

    @classmethod
    def satrdan(cls,matn):
        ism,yosh = matn.split("-")
        return cls(ism, int(yosh))
    @classmethod
    def univer_ozgartir(cls,yangi):
        cls.universitet = yangi
   # @classmethod
    def yil_top(self,joriy):
        return joriy - self.yosh


t = Xodim.satrdan("Bekmirza-23")
print(t.ism,t.yosh)
Xodim.univer_ozgartir("WUIT")
print(t.universitet)
yil = int(input("Joriy yilni kiriting: "))
print(t.yil_top(yil))

