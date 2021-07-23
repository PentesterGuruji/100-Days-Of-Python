# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
#seed = int(input("Enter Random number:- "))
#Write your code below this line 👇
# peoples = len(names)
import random

# ##random.seed(seed)
# person = random.randint(0, peoples - 1)

##using choice function

person = random.choice(names)


# print(f"{names[person]} is going to buy the meal today!")

print( person + " is going to buy the meal today!")

###https://www.askpython.com/python/string/python-string-split-function
# ##split --> .split the list into words
# ##logic first i get the length of the list 
# ##then using the random interger function to get the  one random number in the list --> but the problem is that len function counts like normal ,, and it creates a problem "out of range"  to fix this subtracting 1 from the random number to make it correct .

### ex if list is name{'guruji', 'peru' , 'hai'}
### there is 3 items means length is 3
# ##but you can't select 3 in that list coz python start with zero

# ##then using that random number to fetch the item in the list list[number]

