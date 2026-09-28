class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    @property
    def ism(self):
        return self.__ism

    @ism.setter
    def ism(self, yangi):
        if not yangi.strip():
            raise ValueError("Ism bo'sh bo'lishi mumkin emas")
        self.__ism = yangi

    @property
    def yosh(self):
        return self.__yosh

    @yosh.setter
    def yosh(self, yangi):
        if not 0 <= yangi <= 120:
            raise ValueError("Yosh 0 dan 120 gacha bo'lishi kerak")
        self.__yosh = yangi

    def get_info(self):
        print(f"{self.ism.title()} ismli talabaning yoshi: {self.yosh}")


while True:
    try:
        ism = input("Ism kiriting: ")
        yosh = int(input("Yoshni kiriting: "))
        talaba = Talaba(ism, yosh)
        break
    except ValueError as xato:
        print(f"Xato: {xato}. Qaytadan urinib ko'ring.")

talaba.get_info()

while True:
    try:
        yangi = int(input("Yangi yoshni kiriting: "))
        talaba.yosh = yangi
        break
    except ValueError as xato:
        print(f"Xato: {xato}. Qaytadan urinib ko'ring.")

talaba.get_info()