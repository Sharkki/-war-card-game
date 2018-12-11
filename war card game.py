"""Card game 'war'.
Two persons play against each other. For each round players compare each others cards. The one who got major card wins.
If two cards of the opponents are equal they compare the next pair of the cards.
The winner of the each round collect all the cards that have been played."""

# import
import games
import cards


class WarCard(cards.Card):
    """A model of a card for the game"""

    @property  # card value
    def value(self):
        return WarCard.RANKS.index(self.rank) + 2


class WarDeck(cards.Deck):
    """A model of a deck for the game"""
    MIN_CARDS = 4  # minimum number of cards in the deck when it is still possible to continue the game

    def populate(self):
        """Populates a deck with all possible cards"""
        for suit in WarCard.SUITS:
            for rank in WarCard.RANKS:
                self.add(WarCard(rank, suit))

    @property  # cards left in the deck
    def cards_left(self):
        return len(self.cards)


class WarHand(cards.Hand):
    """A model of player's hand in the game (cards in player's hand)"""

    def __init__(self, name):
        """Initializes player's hand in the game"""
        super().__init__()
        self.name = name

    @property  # sum of player's cards
    def total(self):
        total = 0
        for card in self.cards:
            total += card.value
        return total

    def __str__(self):
        """Prints player's hand in the terminal"""
        # return self.name + ":\t" + super().__str__() + "(" + str(self.total) + ")"
        return '{}: {} ({})'.format(self.name, super().__str__(), str(self.total))


class WarPlayer(WarHand):
    """A model of a player in the game"""

    def __init__(self, name, captured_cards=0):
        """Initializes a player"""
        super().__init__(name)
        self.captured_cards = captured_cards  # cards that have been collected during the game
        
    def lose(self):
        """Prints 'lose' massage for a player in the terminal"""
        print(self.name, "loses.")

    def win(self):
        """Prints 'win' message for a player in the terminal"""
        print(self.name, "wins.")

    @property  # how many cards do player have at the moment
    def current_cards(self):
        return len(self.cards)
        

class WarGame:
    """A model of 'war' card game"""

    def __init__(self, names):
        """Initializes the game"""
        self.players = []
        for name in names:
            player = WarPlayer(name)
            self.players.append(player)
        self.deck = WarDeck()
        self.deck.populate()
        self.deck.shuffle()

    def reshuffle(self):
        """Reshuffles the deck"""
        self.deck.clear()
        self.deck.populate()
        self.deck.shuffle()

    def __additional_cards(self, player):
        """Deals additional card to a player"""
        self.deck.deal([player])
        print(player)

    def play(self):
        """Controls each game round"""
        self.deck.deal(self.players)
        print("One card for each player:")
        for player in self.players:
            print(player)

        print("\nComparing cards:", end=" ")
        while self.players[0].total == self.players[1].total:
            print("the same value of the cards. One more card for each player:")
            for player in self.players:
                self.__additional_cards(player)
        all_current_cards = self.players[0].current_cards + self.players[1].current_cards
        if self.players[0].total > self.players[1].total:
            self.players[0].win()
            self.players[0].captured_cards += all_current_cards
            print('{}, you have captured {} cards.'.format(self.players[0].name, all_current_cards))
        else:
            self.players[1].win()
            self.players[1].captured_cards += all_current_cards
            print('{}, you have captured {} cards.'.format(self.players[1].name, all_current_cards))
        # clear all player's cards
        for player in self.players:
            player.clear()


def main():
    """Creates and controls the game"""
    print("\t\tWelcome to the 'War' card game! (2 players only)\n")
    names = []
    for i in range(2):
        name = input("Enter the name of the player " + str(i+1) + ": ")
        names.append(name)

    game = WarGame(names)

    again = None
    while again != "n":
        if game.deck.cards_left <= WarDeck.MIN_CARDS:
            print("\nThere are too little cards left in the deck ({}). Reshuffling.".format(WarDeck.MIN_CARDS))
            game.reshuffle()
        print("\nNow there are:", game.deck.cards_left, "cards in the deck.")
        game.play()
        print("\n\tStatistics:")
        print('{} - {}.'.format(game.players[0].name, game.players[0].captured_cards))
        print('{} - {}.'.format(game.players[1].name, game.players[1].captured_cards))
        again = games.ask_yes_no("\nContinue? (y/n): ")
    print("\n\t General statistics:")
    print('{} - {}.'.format(game.players[0].name, game.players[0].captured_cards))
    print('{} - {}.'.format(game.players[1].name, game.players[1].captured_cards))


main()
input("\nPress the enter key to exit: ")
