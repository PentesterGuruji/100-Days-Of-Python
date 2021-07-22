print("Welcome to BMI CALCULATOR 2.0")
weight = float(input("Enter your weight in kg: "))
height = float(input ("Enter your height in m: "))

bmi = round(weight/height**2)

# if bmi> 35:
#     print(f"Your BMI is {bmi}, you are clinically obese.")
# elif bmi > 30:
#     print(f"Your BMI is {bmi}, you are obese.")
# elif bmi > 25:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi > 18.5:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# else:
#     print(f"Your BMI is {bmi}, you are underweight.")

#===Another  way ===>


if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

    
