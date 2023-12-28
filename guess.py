import sys
import random

def again():
    pl_again = input("If you want to play again, press 'y' or 'x' to exit: ").lower()
    if pl_again not in ["y", "x"]:
        print("You only have two options: 'y' to play again and 'x' to exit. Please check your input.")
        return again()
    else:
        if pl_again == "y":
            return play_guessing_game()
        else:
            sys.exit()

def play_guessing_game():
    easy_att = 9
    hard_att = 4

    PY_NUM = random.randrange(1, 101)

    def guess(att_rang):
        user_guess = input("Enter your guess: ")
        if not user_guess.isdigit():
            print("You have to enter whole numbers (1, 2, ...40...80..100)")
            return guess(att_rang)

        if att_rang == 0:
            print(f"You have lost, you are out of attempts\nMy number was {PY_NUM}")
            again()

        elif int(user_guess) == PY_NUM:
            print(f"You have {att_rang} attempt left\nYou guessed right! My number was: {PY_NUM}")
            again()

        elif int(user_guess) > PY_NUM:
            print(f"You have {att_rang} attempt left\nToo high")
        else:
            print(f"You have {att_rang} attempt left\nToo low")

    print("I have a number between 1 and 100 in my head")

    hard_or_easy = input("If you want to play guessing, choose between hard and easy.\nPress 'H' for hard level and 'Y' for easy level: ").lower()
    if hard_or_easy not in ["y", "h"]:
        print("You only have two options: 'Y' or 'H'. Please check your input.")
        return play_guessing_game()
    else:
        if hard_or_easy == "h":
            for _ in range(5):
                guess(hard_att)
                hard_att -= 1
        else:
            for _ in range(10):
                guess(easy_att)
                easy_att -= 1

play_guessing_game()
