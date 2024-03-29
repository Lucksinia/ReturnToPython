"""
Bagels! game implementation. Shoud also implement character-by-character
for style points...
"""
from random import shuffle
from prettify.prettify import ochprint

DIGITS = 3  # Number of digits in number.
GUESSES = 10  # all posibble guesses

ochprint(
    f"""Number guessing game in Terminal!
By Lucksinia, denni334334@gmail.com

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
I am thinking of a {DIGITS}-digit number, with no repeated digits watsoever!
Try to guess it in {GUESSES} guesses with the help of the following clues:

    Pico    : One digit is correct, but in the wrong position.
    Fermi   : One digit is correct and in the right position.
    Bagels  : No digits is correct.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
)


def get_secret():
    """Generates nuber based on shuffled list of allowed digits and their number

    :return str: final number of n digits.
    """
    numbers = list("1234567890")
    shuffle(numbers)
    secret = ""
    for i in range(DIGITS):
        secret += str(numbers[i])
    return secret


def get_clues(secret, guess):
    """Find and compare all user guess ang generate string of clues based on
    rules of the game.

    :param str secret: right answer generated by program.
    :param str guess: user's guessed number in string format.
    :return str: string of clues based on alphabetical order.
    """
    if guess == secret:
        return "That's Right! Congratulations!"

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            clues.append("Fermi ")
        elif guess[i] in secret:
            clues.append("Pico ")
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return "".join(clues)


def gameloop():
    """Main Gameloop logic for Bagels!"""
    while True:
        secret = get_secret()
        ochprint(f"I have thought up a number.\n")
        ochprint(f"You have {GUESSES} guesses to get it right.\n")
        guessn = 1
        while guessn <= GUESSES:
            guess = ""
            while len(guess) != DIGITS or not guess.isdecimal():
                ochprint(f"Guess #{guessn}:\n")
                guess = input("~> ")

            clues = get_clues(secret, guess)
            print(clues)
            guessn += 1

            if guess == secret:
                break
            if guessn > GUESSES:
                ochprint("You ran out of guesses...\n")
                ochprint(f"Correct answer was: {secret}.\n")

        ochprint("Do you want to play another game?(y/n):")
        if not input("~> ").lower().startswith("y"):
            break
    ochprint("\nThank you for playing!")


gameloop()
