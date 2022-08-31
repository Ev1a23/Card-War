# Class to define a game deck
import random
from Types import suits, ranks
from CardClass import Card


class Deck:

    def __init__(self):
        self.all_cards = []  # list to store all the cards in the game
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    # Method to shuffle the deck
    def shuffle(self):
        random.shuffle(self.all_cards)

    # Method to deal one card of the deck
    def deal_one(self):
        return self.all_cards.pop(0)
