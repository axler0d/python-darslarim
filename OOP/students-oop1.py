class Talaba:
    def __init__(self,ism,familiya,yosh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
    def get_info(self):
        return f"{self.ism} {self.familiya} {self.yosh}"
class Fan:
    def __init__(self,nomi):
        self.nomi=  nomi
        self.talaba_son = 0
    def add_student(self,talaba):
        self.talaba_son += 1
    def remove_student(self,talaba):
        self.talaba_son -= 1
matematika = Fan("Matematika")
talaba1 = Talaba("sardor","xolbotayev",21)
talaba2 = Talaba("Bekmirza","Madaminov",23)
print(talaba1.get_info())
matematika.add_student(talaba1)
matematika.add_student(talaba2)
print(f"{matematika.nomi} fanida {matematika.talaba_son} ta talaba bor")
matematika.remove_student(talaba1)
print(f"{matematika.nomi} fanida {matematika.talaba_son} ta talaba bor")