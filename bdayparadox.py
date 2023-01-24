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
        To express that, we can generate 100 000 simulations from wich we
        then extrapolate probabylity for such occurence. 
    """
    )

    Months = {
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    }

    while True:
        print("How many birthdays shoud we generate?")
        responce = input("~> ")
        if responce.isdecimal() and (0 < int(responce) <= 100):
            numbdays = int(responce)
            break
    print()
    print(f"There have been {numbdays} Birthdays generated:")
    birthdays = get_birthdates(numbdays)
    for i, birthday in enumerate(birthdays):
        if i != 0:
            print(", ", end="")
            monthname = Months[birthday.month - 1]
            dateText = f"{monthname} {birthday.day}"
            print(dateText, end="")
    print("\n")
    match = get_matched(birthdays)

    print("In this simulation, ", end="")
    if match != None:
        monthname = Months[match.month - 1]
