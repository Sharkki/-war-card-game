"""This module contains class 'Player' and functions common for a great number of different games"""


class Player:
    """A model of a player in a game"""

    def __init__(self, name, score=0):
        """Initializes a player"""
        self.name = name
        self.score = score

    def __str__(self):
        """Prints a player in the terminal"""
        return '{}: {}'.format(self.name, str(self.score))


def ask_yes_no(question):
    """Asks question 'yes/no'. Possible answers - y, n"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Requests a number in the range 'low:high'"""
    response = None
    while response not in range(low, high):
        try:
            response = int(input(question))
        except ValueError:
            print("Acceptable values - from",  low, "to", high-1, "!")
            continue
        if response not in range(low, high):
            print("Acceptable values - from", low, "to", high - 1, "!")
    return response


if __name__ == "__main__":
    print("This module contains class 'Player' and functions common for a great number of different games")
    input('Press any key to exit: ')

