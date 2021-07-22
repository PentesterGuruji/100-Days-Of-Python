age = input("What is your current age? ")
print("If you lucky enough to live 90 years ..")

# days = 365
# weeks = 52
# months = 12
age = int(age)
days = 365*90 - 365*age
weeks = 52*90 - 52*age
months = 12*90 - 12*age

print(f"You have {days} days, {weeks} weeks, {months} months left .. ") 
print("value your time buddy ;)")

#===============Another way ============>

age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = 365*years_remaining
weeks_remaning = 52 * years_remaining
months_remaining = 12 * years_remaining

message = f"You have {days_remaining} days, {weeks_remaning} weeks, {months_remaining} months"

print(message)