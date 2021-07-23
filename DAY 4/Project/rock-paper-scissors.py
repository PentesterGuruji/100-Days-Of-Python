import random

print("Are you ready for rock paper scissors Game?")
print('''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/

 '''
)

human = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer = random.randint(0, 2)


if human == 0:
    print('''You choose Rock,
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif human == 1:
    print('''You choose Paper,
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')


elif human == 2 :
    print('''You choose Scissors,

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

else:
    print("Please Enter Correct Option.")





if computer == 0:
    print('''Computer chose Rock,
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif computer == 1:
    print('''Computer chose Paper,
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

else:
    print('''Computer chose Scissors,

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')


if human == computer:
    print("Draw")
elif (human == 1 and computer == 0) or (human == 0 and computer == 2) or (human == 2 and computer == 1):
    print("WON")

else:
    print("LOSE")