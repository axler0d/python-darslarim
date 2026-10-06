class User:

    @staticmethod
    def login_tek(login):
        if login.isdigit():
            return False
        return True

    @staticmethod
    def parol_tekshir(parol):
        if len(parol) < 7:
            return False
        return True


ism = input("Ismingizni kiriting: ")
familiya = input("Familiyangizni kiriting: ")

login_natija = User.login_tek(ism)
parol_natija = User.parol_tekshir(familiya)

if login_natija:
    print("Login to'g'ri kiritilgan")
else:
    print("Login xato")

if parol_natija:
    print("Parol to'g'ri")
else:
    print("Parol uzunligi kichik")




