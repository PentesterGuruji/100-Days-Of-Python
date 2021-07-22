print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to the Treasure island.\nYour machine is to find the treasure.")

input1 = input("You're on the mid of road where you wanna go? left or right :-\n").lower()

if input1 == "left":
    input2 = input("Now you seeing your objective.\nBut the problem is now there is lake between your target\nNow What you wanna do swim or wait for the boat to come? swim or wait:-\n").lower()
    if input2 == "swim":
        print("Now you are reached you target.\nNow you are seeing three doors , color of doors are as follows:- red, blue, yellow?")    
        input3 = input("Which door you wanna open? red, blue, yellow :-\n").lower()
        if input3 == "yellow":
            print("You found the tressure .. You win!!1")
            
        else:
            print("Game Over.")
        

    else:
        print("Game over. You are waiting till die.")


else:
    print("Game Over .")