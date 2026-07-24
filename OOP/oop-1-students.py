class Talaba:
    def __init__(self, ism, familiya, yosh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
    def __repr__(self):
        return f"{self.ism} {self.familiya}, {self.yosh} yoshda"
talaba1 = Talaba("Ali", "Valiyev", 20)
talaba2 = Talaba("Vali", "Aliyev", 21)

print(talaba1)
print(str(talaba1))
print(repr(talaba1))
print([talaba1])
