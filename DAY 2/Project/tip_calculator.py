print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12, 15, ..?  ")
people = input("How many people to split the bill? ")


# bill = float(input("What was the total bill? $"))
# percentage = int(input("What percentage tip would you like to give? 10, 12, 15, ..?  "))
# people = int(input("How many people to split the bill? "))

# testing = bill + (bill*percentage/100)/people



final_bill = (float(bill) + float(bill)*int(percentage)/100)/int(people)

result = (round(final_bill, 2))

print(f"Each person should pay: ${result}")


#===========Another way of doing ====>

bill_with_tip = float(bill) * ((int(percentage)+100)/100)
contri = round(bill_with_tip/int(people), 2)
print("Each person should pay: $ " + str(contri))

