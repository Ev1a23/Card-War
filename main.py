import random
import Player, Deck, Card

# a dictonary to store every card score
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

# A tuple to store which kinds of suits a card can have
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

# A tuple to store which kinds of rank a card can have
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

# Game Setup
p1 = Player('One')
p2 = Player('Two')
game_deck = Deck()
game_deck.shuffle()
# Divide the cards between the players
for x in range(26):
    p1.add_cards(game_deck.deal_one())
    p2.add_cards(game_deck.deal_one())
print(p1.all_cards[0])
print(p2.all_cards[0])
# Boolean to store if the game should be played
game_on = True
# Counter to keep track of which round is it
round_num = 0
# Boolean to get into checking the cards of each player, if there values aren't equal, it'll change to False and exit
# the loop, else it will stay True
at_war = True
# Actual Game
while game_on:
    round_num += 1
    print(f'Round {round_num}')
    if len(p1.all_cards) == 0:
        print(f'Player {p1.name} Is Out Of Cards, Player {p2.name} Wins!')
        game_on = False
        break

    if len(p2.all_cards) == 0:
        print(f'Player {p2.name} Is Out Of Cards, Player {p1.name} Wins!')
        game_on = False
        break

    p1_cards = [p1.remove_one()]
    p2_cards = [p2.remove_one()]

    at_war = True
    while at_war:
        print(f'Player {p1.name} card: {p1_cards[-1]}, Player {p2.name} card: {p2_cards[-1]} ')
        if p1_cards[-1].value > p2_cards[-1].value:
            p1.add_cards(p1_cards)
            p1.add_cards(p2_cards)
            at_war = False
        elif p1_cards[-1].value < p2_cards[-1].value:
            p2.add_cards(p2_cards)
            p2.add_cards(p1_cards)
            at_war = False
        else:
            print('WAR!')

            # To shorten a bit the game, if a player can't draw a card on a war, he loses immediately, and on a war
            # each needs to draw 5 cards instead of 3 on the original game
            if len(p1.all_cards) < 5:
                print(f'Player {p1.name} Unable To Declare War')
                print(f'Player {p2.name} Wins!')
                game_on = False
                break
            elif len(p2.all_cards) < 5:
                print(f'Player {p2.name} Unable To Declare War')
                print(f'Player {p1.name} Wins!')
                game_on = False
                break
            else:
                for num in range(5):
                    p1_cards.append(p1.remove_one())
                    p2_cards.append(p2.remove_one())