

from os import system, name
# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

from hangman_word import word_list
from hangman_art import stages,logo
import random

print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
#print(f'Pssst, the solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"


Guessed_letters = ""

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    clear()

    if guess in Guessed_letters:
                print(f"You have already guessed {guess}")
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            Guessed_letters += guess
            
    

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])