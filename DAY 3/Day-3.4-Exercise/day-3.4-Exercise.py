print("Welcome to python pizza shop.")

size = input("Let's order the pizza\nWhich pizza you wanna order? Small(S), Medium(M), Large (L): ")
add_pepperoni = input("Do you want extra perpperoni? Y or N: ")
cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill += 15
    # if add_pepperoni == "Y":
    #     bill += 2
    

elif size == "M":
    bill += 20
    # if add_pepperoni == "Y":
    #     bill +=3

else :
    bill +=25
    # if add_pepperoni == "Y":
    #     bill +=3

if cheese == "Y":
    bill += 1

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill +=3


print(f"Your final bill is: {bill}$.")







