import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

a_letters = int(input("How many letters would you like in your password?\n"))

a_numbers = int(input("How many numbers would you like in your password?\n"))

a_symbols = int(input("How many symbols would you like in your password?\n"))

password = ""

for chars in range ( 1, a_letters + 1):
    password += random.choice(letters)

for chars in range ( 1, a_numbers + 1):
    password += random.choice(numbers)

for chars in range(1,a_symbols + 1) :
    password += random.choice(symbols)

print(f"Your easy password is {password}")

## For completely random password instead of strings we have to use list

password_list = []

for chars in range ( 1, a_letters + 1):
    password_list.append(random.choice(letters))

for chars in range ( 1, a_numbers + 1):
    password_list.append(random.choice(numbers))

for chars in range(1,a_symbols + 1) :
    password_list.append(random.choice(symbols))



print(f"Your hard password is {a}")