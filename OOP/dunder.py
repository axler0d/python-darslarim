class User:
    def __init__(self,ism,familiya,yosh,instut,baho):
        self.ism = ism
        self.yosh = yosh
        self.instut = instut
        self.baho = baho
        self.familiya = familiya
    def __str__(self):
        return f"""Ism: {self.ism.title()}, 
Yosh:{self.yosh},
Institut: {self.instut},
Baho:{self.baho} 
{self.familiya.title()}"""
    def __len__(self):
        return len(self.ism + " " + self.familiya)
    def __eq__(self, other):
        return self.instut == other.instut and self.familiya == other.familiya and self.ism == other.ism
    def __add__(self, other):
        return self.baho + other.baho
ism = input("admin ismi (login): ")
familiya = input("admin famili")