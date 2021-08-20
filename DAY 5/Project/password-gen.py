import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

a_letters = int(input("How many letters would you like in your password?\n"))

a_numbers = int(input("How many numbers would you like in your password?\n"))

a_symbols = int(input("How many symbols would you like in your password?\n"))


### print(f"{a}")
## b = 
# #c = 

random_letter = ""
random_number = ""
random_symbols = ""
# # # # print(a)

for x in range(0,a_letters):
    oof = letters[random.randint(0,len(letters)) - 1]
    random_letter += oof

for x in range(0,a_numbers):
    oof = numbers[random.randint(0,len(numbers)) - 1]
    random_number += oof

for x in range(0,a_symbols):
    oof = symbols[random.randint(0,len(symbols)) - 1]
    random_symbols += oof


## print(random_letter)
## print(random_number)
# #print(random_symbols)

# random.shuffle(f"{random_letter}")

# print(random_letter)

easy_level = random_letter + random_symbols + random_number 

print(f"Its easy password {easy_level}")

print(''.join(random.sample(easy_level,len(easy_level))))


# for x in range(0,a_letters):
#     doing = letters[random.randint(0,len(letters)) - 1]
#     random_letter 

# for x in range(0,a_numbers):
# #     oof = numbers[random.randint(0,len(numbers)) - 1]
#     random_number += oof

# for x in range(0,a_symbols):
#     oof = symbols[random.randint(0,len(symbols)) - 1]
#     random_symbols += oof