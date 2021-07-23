## Virtual coin tosser using random module :)

# import random
# num = random.randint(0,1)
# if num == 0:
#     print("Heads")
# else:
#     print("Tails")

### using seeds method to check outcomes 
import random
seeds = int(input("Enter the random number:-\n"))

random.seed(seeds)
num = random.randint(0, 1)
if num == 0:
    print("Heads")
else:
    print("Tails")

print("To check the results again enter the same number again")