def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


while True:

    while True:
        try:
            x = int(input("Enter a positive integer: "))

            if x <= 0:
                print("Iltimos, 0 dan katta butun son kiriting!")
                continue

            break

        except ValueError:
            print("Iltimos, 0 dan katta butun son kiriting!")

    if is_prime(x):
        print(f"{x} is a prime number.")
    else:
        print(f"{x} is not a prime number.")

    javob = input("Yana tekshirishni xohlaysizmi? (ha/yo'q): ").lower()

    if javob != "ha":
        print("Dastur tugadi.")
        break