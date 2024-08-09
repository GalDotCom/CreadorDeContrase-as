import random
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input("¿Cuántos caracteres quieres que tenga tu contraseña? "))
password = ""
for i in range(length):
    password += random.choice(characters)
print("Tu nueva contraseña es:", password)
