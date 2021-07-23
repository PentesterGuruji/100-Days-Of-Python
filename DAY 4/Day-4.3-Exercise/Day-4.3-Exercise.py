
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
columns = int(position[0]) - 1
row = int(position[1]) - 1 

#ALWAYS REMEMBER HORIZONTAL( -->) ROWS AND VERTICAL COLUMNS( DOWN ARROW) 

# map[row][columns] = "X"
## https://riptutorial.com/python/example/11713/accessing-values-in-nested-list


#row uthao and then uske andr ke value ko change karo
selected_row = map[row]

selected_row[columns] = "X"



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")