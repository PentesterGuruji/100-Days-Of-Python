#len of strings

#len of number?
# len(12345)
# it will come with error

#-> DATA TYPES

#Strings ex. "Hello"

#we can pull each character individually using [] this method is called subscripting
#ex print("Hello"[0])

#Printing the "o"

print("HELLO"[4])
print("HELLO"[-1])

#if numbers are in "" it will treated as strings

print("1234" + "345") # this is just catenated two strings instead of doing mathematical operations

#Integers ( number without any decimals all postive or negative)

print(123 + 345)

# _ is not interpreted it will remove by computer , we can use this as comma to differ between large integers

print(1_25_000 + 1)

#Floating point number ( decimal point )
# 3.14159

# Boolean ( two possible values True False)

# _______________________

#type() to check type of variable
# len function

# num_char = len(input("what is your name?"))
# # print("Your name has " + num_char + " characters.")
# print(type(num_char))

# #changing int to str 

# new = str(num_char)

# print("Your name has " + new + " characters.")


a = 1234
print(type(a))
b = str(1234) # int to str
print(type(b))
c = float(1234) #int to float
print(type(c))

print(70 + float("100.05")) # output is 170.5

print(str(70)+ str(100)) # catenate simply


#Mathematical operators

# 7-5
# 3+5
# 3*5
# 6/2 you will get float like 3.0 
# 3**5 (exponent)

# PEMDASLR ( LEFT TO RIGHT)

# paranthesis ()
# expontial **
# multiplication * # divide /
# plus + # minus - 

print(3 * 3 + 3/3 - 3)

#instead of 7 you want 3 in answer

print(3* (3+3)/3 - 3)


# Rounding off the numbers

#like 19.5 
# 8/3 is 2.666666 if we convert into interger it will give 2 
# in maths we do 2.67

#round() function

print(round(8/3)) # this will give 2
print(round(8/3) , 2 ) # 2 is two decimal value answer is 2.67

#floating division 

#traditonally if we don't need decimals 
#we do like this

print(int(8/3))

# with floating division // you can output answer without decimals
print(8/3)
print(8//3)
print(type(8/3)) # this is float
print(type(8//3)) # this is int

## more operation

result = 4 / 2
#now we want to divide it by 2 again
result /= 2  # this will divide the result / 2
# instead of using result = result/2 ==> /=
# -= ,, +=
print(result)


## incorpoarting different data types

#f-string --> in front of string we add f

score = 0 
heigt = 1.8
isWinning = True

# print("Your score is " + str(score) ) #This shit is paining to ass for every data type we have to convert in into strings

# using f-strings ( use f in front and put {variable name})

print(f"Your score is {score} , your height is {heigt} , you are winning {isWinning}")
