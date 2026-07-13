def son_top(a):
    if a == 1:
        return 1
    else:
        return a + son_top(a - 1)
while True:
    try:
        a = int(input("Enter a number: "))
        if a < 1:
            print("Please enter a positive integer.")
            continue
        result = son_top(a)
        print(f"The sum of numbers from 1 to {a} is: {result}")
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
x = int(input("Enter a number to check if it is prime: "))
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if is_prime(x):
    print(f"{x} is a prime number.")
else:
    print(f"{x} is not a prime number.")
