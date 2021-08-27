from art import logo
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

from random import randint


COMPUTER_GUESS = randint(1,100)

level = input("Choose a difficulty. Type 'easy' or 'hard': ")

# print(f"Pssst computer guess {COMPUTER_GUESS}")

live = 0

def lives():
    if level == "hard":
        return live + 5

    elif level == "easy":
        return live + 10

live += lives()

def status():
    if live != 0:
        return "Guess again"
    
    else:
        return "You ran out of lives.. 😥"

is_answer_correct = False

while range(0,live) and not is_answer_correct:
    print (f"You have {live} attempt guess left to guess.")
    user_guess = int(input("Make a guess.. :- "))
    live -= 1
    def compare(COMPUTER_GUESS,user_guess):
        '''Comparing the guesses :)'''

        if COMPUTER_GUESS > user_guess:
            return "Too low"
        
        elif COMPUTER_GUESS < user_guess:
            return "Too high"
        
        elif COMPUTER_GUESS == user_guess:
            return "You got it...\n Winner 🤩"

    result = compare(COMPUTER_GUESS,user_guess)
    print(result)

    if "got" in result:
        is_answer_correct = True
    
    else:
        print(status())

    




