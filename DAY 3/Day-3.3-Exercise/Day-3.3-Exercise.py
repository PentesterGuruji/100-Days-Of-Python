print("Checking a year is leap or not!")
##### year = input("Enter the year:- ")
year = int(input("Enter the year:- "))

##### if len(year) != 4:
#####     print(f"Enter correct year dude.. {year} this doesn't seems to be year.")
#####     exit()

##### year = int(year)

# if year%100 != 0:
#     if year%4 != 0:
#         print(f"Not leap year.")
#     else:
#         print(f"Leap year.")

# elif year%100 == 0:
#     if year%400 == 0:
#         print(f"Leap year.")
#     else:
#         print(f"Not leap year.")

# else:
#     print("crashed")

#Checking the year is leap or not
#checking only the first condition divisible by 4 means no remainder

# Leap years rule:
#     Add an extra day every 4 years
#     Skip it if it's a new century
#     Unless the century is divisble by 400

# year is divisible by 4  then check year is divisible by 100 if yes then check year is divisible by 400  then its leap if not its not leap , if not divisible by 100 then its leap , if not divisble by  4 is not leap



## every century leap year is skip if they are divisible by 400

###=============Another way ==========>




if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("Leap year.")
        else:
            print("Not a Leap year.")
    else:
        print("Leap year.")

else:
    print("Not a leap year.")