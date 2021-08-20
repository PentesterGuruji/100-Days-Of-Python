# LOOP

# allows us to execute code multiple times

#FOR LOOP




fruits = [ "apple", "Peach", "Pera"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# it is assigning variable name fruit to different items in fruits list and then printing one by one

### for loop via range function


# for number in range(start, stop , step)
for number in range(1, 10):
    print(number) # it gonna print 1 to 9 # default is 1 step


# now i want number after 2 Steps
for number in range (1,10, 2):
    print(number)
