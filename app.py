import random

chars = "abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"

pw_len = int(input("What length would you like: "))
pw_count = int(input("How many password would you like: "))

for x in range(0,pw_count):
    password = ""
    for x in range(0,pw_len):
        pw_char = random.choice(chars)
        password += pw_char

    print("Password:", password)
