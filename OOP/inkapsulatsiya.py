class Bank:
    def __init__(self,balans):
        self.__balans = balans
    @property
    def balans_korish(self):
        return self.__balans

    def pul_qoshish(self,summa):
        self.__balans += summa
  
    def pul_yechish(self,summa):
        if summa <= self.__balans:
            self.__balans -= summa
        else:
            print("Mablag' yetarli emas")

bank = Bank(1000000)
print('Mavjud summa: ',bank.balans_korish)
summa = int(input("Yechmoqchi bo'lgan summani kiriting: "))
#print("Pul yechilmasdan oldingi summa: ",bank.balans_korish())
bank.pul_yechish(summa)
print("Keyingi summa: ",bank.balans_korish)
bank.pul_qoshish(150000)
print("Keyingi summa: ",bank.balans_korish)