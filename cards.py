"""This module contains basic classes for 'war' card game"""


class Card:
    """A model of playing card"""
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
    SUITS = ["hearts", "clubs", "spades", "diamonds"]

    def __init__(self, rank, suit, face_up=True):
        """Initializes playing card"""
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        """Prints playing card in the terminal"""
        if self.is_face_up:
            response = "<{} {}>".format(self.rank, self.suit)
        else:
            response = '<XX>'
        return response

    def flip(self):
        """Flips playing card"""
        self.is_face_up = not self.is_face_up


class Hand:
    """A model of a set of cards (hand) of a single player"""

    def __init__(self):
        """Initializes player's hand"""
        self.cards = []

    def __str__(self):
        """Prints player's hand in the terminal"""
        if self.cards:
            response = ""
            for card in self.cards:
                response += str(card) + ' '
        else:
            response = '<empty>'
        return response

    def clear(self):
        """Clears player's hand"""
        self.cards = []

    def add(self, card):
        """Adds a card to player's hand"""
        self.cards.append(card)

    def give(self, card, other_hand):
        """Transfers a card from player's hand to another player's hand"""
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    """A model of a deck of playing cards"""

    def populate(self):
        """Populates a deck with all possible playing cards"""
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        """Shuffles a deck of cards"""
        import random
        random.shuffle(self.cards) 

    def deal(self, hands, per_hand=1):
        """Deals cards to players (hands)"""
        for stage in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand) 
                else:
                    print("Can't deal cards anymore: deck is empty!")
                    

if __name__ == "__main__":
    print('This module contains basic classes for the card game.')
    input('Press any key to exit: ')

