class Talaba:
    def __init__(self,ism,familiya,baho):
        self.ism = ism
        self.familiya = familiya
        self.__baho = baho
    @property
    def ball(self):
        return f"{self.ism.title()} {self.familiya.title()}ning bahosi {self.__baho}"
    @ball.setter
    def ball(self,yangi):
        if yangi >= 0 and yangi <= 100:
            self.__baho = yangi
        else:
            print("Baho noto'g'ri")
talaba = Talaba("bekmirza",'madaminov',75)
print(talaba.ball)
talaba.ball = 15
print(talaba.ball)

