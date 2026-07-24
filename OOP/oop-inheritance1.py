class Shaxs:
    def tanishtir(self):
        print("Men oddiy shaxsman")
class Teacher(Shaxs):
    def tanishtir(self):
        super().tanishtir()
        print("Men o'qituvchiman")
inson = Teacher()
inson.tanishtir()

class Telefon:
    def __init__(self,brend):
        self.brend = brend
class Smartfon(Telefon):
    def __init__(self, brend, model):
        super().__init__(brend)
        self.model = model
s = Smartfon("Samsung","S25 Ultra")
print(s.brend)
print("----------------------")
print(s.model)
