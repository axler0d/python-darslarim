class Bank:
    def __init__(self,balans):
        self.__balans = balans
    @property
    def balans(self):
        return self.__balans
    @balans.setter
    def balans(self,yangi):
        if yangi>=0:
            self.__balans = yangi
        else:
            print("Balans manfiy bo'lishi kerak emas!!!")
bank = Bank(2500000)
print(bank.balans)
bank.balans = -2500000
print(bank.balans)