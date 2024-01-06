import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c',
           'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',
           '+', '=', '{', '}', '[', ']', ';', ':', '<', '>', ',', '.', '/', '?']

print("welcome to the password PyPassword Generator.")
number_of_letters = int(input("How many number would you like in your password?\n"))
number_of_symbols = int(input("How many symbols would you like?\n"))
number_of_numbers = int(input("How many number would you like?\n"))

# eascy level

password = ""
for char in range(1, number_of_letters + 1):
    password += random.choice(letters)

for symbol in range(1, number_of_symbols + 1):
    password += random.choice(symbols)

for number in range(1, number_of_numbers + 1):
    password += random.choice(symbols)

print(f"your weak password is: {password}")

# Hard level
password_list = []
for char in range(1, number_of_letters + 1):
    password_list.append(random.choice(letters))

for symbol in range(1, number_of_symbols + 1):
    password_list.append(random.choice(symbols))

for number in range(1, number_of_numbers + 1):
    password_list.append(random.choice(symbols))

# print(password_list)
random.shuffle(password_list)
# print(password_list)

hard_password = ""
for char in password_list:
    hard_password+=char
print(f"your hard password is {hard_password}")
