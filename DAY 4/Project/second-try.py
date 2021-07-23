rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
symbols = [ rock, paper, scissors]
import random
print("Welcome to Rock Paper Scissors Game.")


human = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if (human >=3 or human < 0):
    print("You choose an invalid option !!!")
else:
    print("You choose " + symbols[human])




computer = random.randint(0,2)

# if human == 0:
#     print(rock)
# elif human == 1:
#     print(paper)
# else:
#     print(scissors)

# if computer == 0:
#     print("Computer Chose" + rock)
# elif computer == 1:
#     print("Computer Chose" + paper)
# else:
#     print("Computer Chose" + scissors)

#alternative using lists




print("Computer chose " + symbols[computer])



if computer == human:
    print("Draw")
elif (human == 0 and computer == 2 ) or (human == 2 and computer == 1) or (human == 1 and computer == 0 ):
    print("won")
else:
    print("lose")