def number_guessing():
    """
    Function, that takes no arguments.
    When run, it chooses random number from 0 and 100
    Then, asks to guess it.
    There tree variants:

        * Too high
        * Too low
        * Just rigt

    If user guessed correct number, exit the programm.
    If not, try again.
    """
    from random import randint

    secret = randint(0, 100)
    while answer := int(input("Your guess: ")):
        if answer == secret:
            print(f"That's Right! {answer} is a correct number!")
            break
        elif answer > secret:
            print(f"{answer} is too high!")
        else:
            print(f"{answer} is too low!")


number_guessing()
