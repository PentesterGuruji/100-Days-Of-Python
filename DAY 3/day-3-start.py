#conditional if/else

# if condition:
#     do this
# else:
#     do this

# >= 


########### CODE 1 PLEASE UNCOMMENT IT

# print("Welcome to rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the roolercoaster")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7")
#     else:
#         print("Please pay $12")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

###################### CODE ###################
#comparison operator

#> greater than
#< less than
#>= greater than equal to
#<= less than equal to
#!= not equal to 
#== equal to

# one equal sign  -> it means you are signing this value to this variable
# two equal sign --> it means you are checking one value is equal to other

# modula (%) 7%2 gives remainder
# exercise 1 

#nested if/else statements
# if else ke andar ek orr if /else 

# condition <12 $5 , 12-19 $7 , >18 is $12 then we have to use elif --> we can add many elif


# multiple condition:

# ex - if person wants a picture in rollercoaster they have to pay $3 this is independent of their age  and it means it needs new if condition  not elif

# if condition1:
#     dothis 

# if condition2:
#     do this

# if condition3:
#     do this

################CODE 2 ############


print("Welcome to rollercoaster!")
height = int(input("What is your height in cm? "))
#adding variable bill = 0

bill = 0

if height >= 120:
    print("You can ride the roolercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Young tickets are $7")
    
    elif age >=45 and age <= 55: ##here is combination of two condititon
        bill = 0
        print("Your ticket is free because you are covered in mediclaim.")

    else :
        bill = 12
        print("Adults tickets are $12")
    
    pic = input("Do you wanna photo taken? Y or N  ")
    if pic == "Y":
        bill += 3
    
            # adding 3$ to bill , irrespective to bill
            # bill = bill + 3
        
    print(f"The current bill is ${bill}")

    # keep check on indentation meaning spacing ...
    

else:
    print("Sorry, you have to grow taller before you can ride.")






### logical operator --> combining two or more conditions

# A and B ==> both condition must be true
# C or D ==> only one condition must be true 
# not E ==> reverse the condition



#### now company is saying if anyone have medlife crises..there ticket is free .. according to wiki :- medlife crises age is 45-65 


### ''' tirple quote is good when string is quite big

### ex print('''
# 
# sdfasdf
# '''')

#\'r is good to escape r 
# ex print('you\'re "right"')