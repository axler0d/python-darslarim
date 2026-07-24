print("Kvadrat tenglamaning ildizlarini topish dasturiga xush kelibsiz!")

def son_kiritish(nom):
    while True:
        try:
            return float(input(f"{nom} ni kiriting: "))
        except ValueError:
            print("Iltimos, son kiriting.")

a = son_kiritish("a")
while a == 0:
    print("a 0 ga teng bo'lmasligi kerak. Iltimos, qayta kiriting.")
    a = son_kiritish("a")

b = son_kiritish("b")
c = son_kiritish("c")

print(f"Siz kiritgan tenglama: {a}x^2 + {b}x + {c} = 0")

d = b**2 - 4*a*c
if d < 0:
    print("Tenglamaning haqiqiy ildizlari yo'q.")
elif d == 0:
    x = -b / (2*a)
    print(f"Tenglamaning yagona ildizi: {x}")
else:
    x1 = (-b + d**0.5) / (2*a)
    x2 = (-b - d**0.5) / (2*a)
    print(f"Tenglamaning ildizlari: x1 = {x1}, x2 = {x2}")