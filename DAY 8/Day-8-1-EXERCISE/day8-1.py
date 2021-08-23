###Area cal Exercise

####Write your code below this line 👇


def paint_calc(height,width,cover):
    number_of_can = ( height*width)/cover
    roundoff = round(number_of_can + 0.4)
    print(f"You'll need {roundoff} cans of paint.")
    


### if the number of can is 1.25 round will be 1 but we need 2 . so i am adding 0.4 evertime to get desired round off




############################################

# 
# 
# another way


# import math
# print(int(math.ceil(4.2)))

#https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number


import math



def paint_calc(height,width,cover):
    number_of_can = ( height*width)/cover
    roundoff = math.ceil(number_of_can)
    print(f"You'll need {roundoff} cans of paint.")



####W#rite your code above this line 👆
#### Define a function called paint_calc() so that the code below works.   

# ###🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


