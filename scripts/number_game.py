#Author: Johnny Romano
import random

# generate a number between 1 and 10
secret_num = random.randint(1, 10)
guesses = []

def main():
    while len(guesses) < 5:
        try:
        # get a number guess from the player
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("{} isn't a number!".format(guess))
        else:
            # compare guess to secret number
            if guess == secret_num:
                print("You got it! My number was {}".format(secret_num))
                break
            elif guess > secret_num:
                print("Sorry, try lower!")
            elif guess < secret_num:
                print("Sorry, try higher!")
            guesses.append(guess)
main()
