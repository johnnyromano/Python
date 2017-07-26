#!/usr/bin/env python
"""
    File name: letter_game.py
    Description: Hangman based letter guessing game.
    Author: Johnny Romano
    Email: John.p.romano@gmail.com
    Date created: 13-July-2017
    Date last modified: 25-July-2017
    Python Version: 3.5
"""
import os
import random
import sys

# make a list of words
WORDS = [
    'apple',
    'banana',
    'orange',
    'coconut',
    'strawberry',
    'lime',
    'grapefruit',
    'lemon',
    'kumquat',
    'blueberry',
    'melon'
]

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def draw(misses, correct, word):
    clear()

    print('Strikes: {}/7'.format(len(misses)))
    print('')

    for letter in misses:
        print(letter, end=' ')
    print('\n\n')

    for letter in word:
        if letter in correct:
            print(letter, end='')
        else:
            print('_', end='')

    print('')

def get_guess(guesses):
    while True:
        # take guess
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("You can only guess a single letter!")
        elif guess in guesses:
            print("You've already guess that letter!")
        elif not guess.isalpha():
            print("You can only guess letters!")
        else:
            return guess

def play(done):
    clear()
    # pick a random word
    word = random.choice(WORDS)
    misses = set()
    correct = set()
    word_set = set(word)

    while True:
        draw(misses, correct, word)
        guess = get_guess(misses | correct)

        if guess in word_set:
            correct.add(guess)
            if not word_set.symmetric_difference(correct):
                print("You Win!")
                print("The secret word was {}".format(word))
                done = True
        else:
            misses.add(guess)
            if len(misses) == 7:
                draw(misses, correct, word)
                print("You lost!")
                print("The secret word was {}".format(word))
                done = True

        if done:
            play_again = input("Play again? Y/n ").lower()
            if play_again != 'n':
                return play(done=False)
            else:
                sys.exit()

def welcome():
    start = input("Press enter/return to start or Q to quit ").lower()
    if start == 'q':
        print("Bye!")
        sys.exit()
    else:
        return True

print('Welcome to Letter Guess!')

done = False

while True:
    clear()
    welcome()
    play(done)
