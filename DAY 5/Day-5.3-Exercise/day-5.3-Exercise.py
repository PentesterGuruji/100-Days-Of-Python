evennumber = 0
#Adding even number
for x in range(2,101,2):
    evennumber += x

secondapproach = 0
for x in range(1,101):
    if x % 2 == 0:
        secondapproach +=x
    
print(f"The sum of even number till 100 is:- {evennumber}")

print(f"{secondapproach}")