# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
### 🚨 Don't change the code above 👆

sum_of_heights = 0
total_heights = 0

for n in student_heights:
    sum_of_heights += n
    
for n in student_heights: #functionality of len function
    total_heights += student_heights.count(n) 


## print(sum_of_heights)
## print(total_heights)

average_height = round(sum_of_heights/total_heights)

print(average_height)


# #if we are using it will be very easy
# #len(student_heights)
# #sum(student_heights)


###### solution 

## sum method is same but to get the total number approach is different

## 

# number_of_student = 0

# for x in student_heights:
#     number_of_student += 1

# print(number_of_student)

## conclusion loop will run according to entries in the list..

# so everytime it loop it will add 1 and we get our value:) noice approach too

# my count method is desi jugad 