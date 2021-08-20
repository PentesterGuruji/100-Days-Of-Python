# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highest_score = 0


## max function in loop

for n in student_scores:
    if n > highest_score:
        highest_score = n

print(f"The highest score in the class is : {highest_score}")

## min function in for loop
for n in student_scores:
    if n < highest_score:
        highest_score = n

print(f"The lowest score is {highest_score}")

