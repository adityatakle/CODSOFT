import random

def generate_password(length):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" + "0123456789" + "!@#$%^&*_+"
    password = ''.join(random.choice(characters) for _ in range(length))
    print(password)

print("Strong and Random Password Creator")
length = int(input("Enter the length of the password: "))
generate_password(length)