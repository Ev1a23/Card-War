# Class to define a card
from Types import values


class Card:

    def __init__(self, suit, rank):
        self.suit = str(suit).capitalize()
        self.rank = str(rank).capitalize()
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit