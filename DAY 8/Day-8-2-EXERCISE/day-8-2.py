#Write your code below this line 👇

### my way

# def prime_checker(number):
#     checked = 0
#     for x in range(1, number+1):
#         if number % x == 0:
#             checked += 1

#     if checked == 2 or number == 1:
#         print("It's a prime number.")
    
#     else:
#         print("It's not a prime number.")


## another way

def prime_checker(number):
    is_prime = True
    for i in range(2, number - 1):
        if number % i == 0:
            is_prime = False
    
    if is_prime:
        print("It's a prime number")
    
    else:
        print("It's not a prime number.")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

