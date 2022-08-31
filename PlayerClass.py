# Class to define a player in the game
class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    # Method to remove the top card of the list of cards that a player have
    def remove_one(self):
        return self.all_cards.pop(0)

    # Method to add one card/multiple cards to the list of cards that a player have
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        if len(self.all_cards) != 1:
            return f'Player {self.name} Has {len(self.all_cards)} Cards'
        else:
            return f'Player {self.name} Has 1 Card'
