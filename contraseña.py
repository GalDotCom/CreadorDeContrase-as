import random
ls = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_len = int(input("Cuantos caracteres quieres que tenga tu contraseña? "))
password = ""
for i in range(length):
    password += random.choice(characters)
print("Tu nueva contraseña es:", password)
