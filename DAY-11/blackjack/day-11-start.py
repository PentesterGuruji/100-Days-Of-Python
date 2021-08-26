from art import logo
import random
from os import system

def playgame():
    print (logo)
    user_cards = []
    computer_cards = []


    def deal_card():
        """ Returns random card from the deck."""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return (random.choice(cards))


    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    def calucate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        
        elif sum(cards) > 21:
            if 11 in cards:
                cards.remove(11)
                cards.append(1)

        return sum(cards)
        



    is_stop = False
    while not is_stop:
        user_score = calucate_score(user_cards)
        computer_score = calucate_score(computer_cards)
        print("_______________________________________________________\n")
        print(f"    Your cards: {user_cards} and Your score: {user_score}")
        print("_______________________________________________________\n")
        print(f"     Computer's first card:  {computer_cards[0]}")
        print("_______________________________________________________\n")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_stop = True

        else:
            
            telling = input("Type 'y' to get another card , type 'n' to pass: ") 

            if telling == "y":
                user_cards.append(deal_card())

            elif telling == "n":
                is_stop = True

                
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calucate_score(computer_cards)


    def compare(user_score,computer_score):

        if user_score == computer_score:
            return "_______________________________________________________\nDraw 😌\n_______________________________________________________"

        elif computer_score == 0:
            return "_______________________________________________________\nLoose, opponent has Blackjack 😱\n_______________________________________________________"
        
        elif user_score == 0:
            return "_______________________________________________________\nWinner with a Blackjack 😎\n_______________________________________________________"


        elif  user_score > 21:
            return "_______________________________________________________\nYou went over, You loose 😪\n_______________________________________________________"

        elif computer_score > 21:
            return "_______________________________________________________\nOpponent went over, You win 😁\n_______________________________________________________"
        
        elif computer_score > user_score:
            return "_______________________________________________________\nYou loose 🤐\n_______________________________________________________"

        elif computer_score < user_score:
            print("_______________________________________________________\nYou win 😆\n_______________________________________________________")

        else:
            return "_______________________________________________________\nYou loose 😶\n_______________________________________________________"


    print("_______________________________________________________\n")
    print(f"  Your final hand: {user_cards}, final score: {user_score}")
    print("_______________________________________________________\n")
    print(f"  Computer's final hand: {user_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))




while input("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nDo you want to play a game of Blackjack? Type 'y' or 'n' : ") == "y":
    system('cls')
     
    playgame()