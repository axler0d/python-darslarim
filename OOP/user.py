print("Xush kelibsiz")

class User:
    def __init__(self,login,parol):
        self.login = login
        self.parol = parol

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self,yangi):
        if not yangi.isalpha():
            raise ValueError("Login harflardan iborat bo'lsin")
        self.__login = yangi.lower()

    @property
    def parol(self):
        return self.__parol

    @parol.setter
    def parol(self,yangi):
        if not yangi.strip():
            raise ValueError("Parol bo'sh bo'lmasin")
        self.__parol = yangi

    def parol_almashtir(self,yangi):
        if yangi == self.parol:
            raise ValueError("Eski parol yozdingiz")
        self.parol = yangi

admin_parol = '123456789'
print("XUsh kelibsiz admin")
while True:
        parol = input("parolni kiriting: ")
        if parol != admin_parol:
            print("Parolni xato kiritdingiz, iltimos qayta kiriting: ")
            continue
        else:
            users = {}

            while True:
                try:
                    tanlov = int(input("""
1 - User qo'shish
2 - User qidirish
3 - User o'chirish
4 - Userlarni ko'rish
5 - Chiqish
Tanlovingiz: """))

                except ValueError:
                    print("Iltimos, menyudan raqam kiriting!")
                    continue

                if tanlov == 1:
                    try:
                        login = input("Login: ").strip()

                        if login.lower() == "admin":
                            print("Bu login band!")
                            continue

                        if login.lower() in users:
                            print("Bu login band! Boshqa login kiriting.")
                            continue

                        parol = input("Parol: ")
                        user = User(login, parol)
                        users[user.login] = user
                        print("Foydalanuvchi qo'shildi!")

                    except ValueError as xato:
                        print(xato)

                elif tanlov == 2:
                    nom = input("Qidiriladigan login: ").strip().lower()

                    if nom in users:
                        print("Foydalanuvchi topildi!")
                        print(f"Login: {users[nom].login}")
                    else:
                        print("Bunday foydalanuvchi topilmadi.")

                elif tanlov == 3:
                    nom = input("O'chiriladigan login: ").strip().lower()

                    if nom in users:
                        del users[nom]
                        print("Foydalanuvchi o'chirildi!")
                    else:
                        print("Bunday foydalanuvchi topilmadi.")

                elif tanlov == 4:
                    if users:
                        for raqam, (login, user) in enumerate(users.items(), start=1):
                            print(f"{raqam}. Login: {user.login} | Parol: {user.parol}")
                    else:
                        print("Hozircha foydalanuvchilar yo'q.")

                elif tanlov == 5:
                    print("Goodbye!")
                    break
                else:
                    print("1 dan 5 gacha bo'lgan raqamni tanlang!")
        break
