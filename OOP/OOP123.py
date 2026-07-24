class Employee:
    company_name = "IBM Company"

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"{self.name} {self.salary} $ maosh oladi hamda '{self.company_name}'da dasturchi sifatida ishlaydi"
    #def show(self):
     #   print( f"{self.name} {self.salary} $")
employee1 = Employee('Bekmirza',3000)
employee2 = Employee('Hasan',3000)
#employee1.show()
#employee2.show()
hodimlar = [employee2,employee1]
print("Hodimlar maoshlari")
for hodim in hodimlar:
    print(hodim)
