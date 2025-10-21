import random
letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
symbols = list("!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~")
numbers = list("0123456789")

total_letters = int(input("How many letters would you like in your password?\n"))
total_symbols = int(input("How many symbols would you like?\n"))
total_numbers = int(input("How many numbers would you like?\n"))

password_list = []
for letter in range(1, total_letters + 1):
    password_list += random.choice(letters)

for symbol in range(1, total_symbols + 1):
    password_list += random.choice(symbols)

for number in range(1, total_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

print("".join(password_list))
    
    