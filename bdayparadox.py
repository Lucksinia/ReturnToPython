import random
import datetime


def get_birthdates(numofbd):
    """Generate list of birthday dates based on January 1, 2001.

    :param int numofbd: Number of birthdays to generate.
    :return list birthdates: List of birthdays.
    """
    birthdates = []
    for date in numofbd:
        start_of_year = datetime.date(2001, 1, 1)
        randomnumb = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + randomnumb
        birthdates.append(birthday)
    return birthdates


def get_matched(birthdates):
    if len(birthdates) == len(set(birthdates)):
        return None

    for a, bdayA in enumerate(birthdates):
        for b, bdayB in enumerate(birthdates[a + 1 :]):
            if bdayA == bdayB:
                return bdayA


def main():
    print(
        """Birthday Paradox, by Lucksinia
        In a group of N people, odds of some of them having birthdays on the
        same day is suprisingly large
        To express that, we can generate 100000 simulations   
    """
    )
