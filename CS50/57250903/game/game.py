import random
import sys

def main():
    get_guess()

def get_level():

    while True:
        try:
            level = int(input("Level: "))

            if level < 0:
                raise ValueError
            else:
                level_random = random.randint(1,level)
                break
        except ValueError:
            continue

    return level_random

def get_guess():

    level_random = get_level()

    while True:
        try:
            guess = int(input("Guess: "))

            if guess < 0:
                raise ValueError
            if guess == level_random:
                sys.exit("Just right!")
                break
            elif guess <= level_random:
                print("Too small!")
            else:
                print("Too large!")
        except ValueError:
            continue

main()
