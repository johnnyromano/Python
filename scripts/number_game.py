#Author: Johnny Romano
import random

def game():
    # generate a number between 1 and 10
    secret_num = random.randint(1, 10)
    guesses = []

    while len(guesses) < 5:
        try:
        # get a number guess from the player
            guess = int(input("\nGuess a number between 1 and 10: "))
        # catch if not number
        except ValueError:
            print("{} isn't a number!".format(guess))
        else:
            # add guess to guesses
            guesses.append(guess)
            # compare guess to secret number
            if guess == secret_num:
                print("You got it! {} was my number.\nIt took you {} attempts".format(secret_num, len(guesses)))
                break
            elif guess > secret_num:
                print("Try lower than {}!".format(guess))
            elif guess < secret_num:
                print("Try higher than {}!".format(guess))
    else:
        print("\nYou didn't get it! My number was {}.".format(secret_num))

    play_again = input("\nDo you want to play again? Y/n ")
    if play_again.lower() != 'n':
        game()
    else:
        print("See ya later!")
game()
