import itertools
from enum import Enum

_ranks = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
# or  ranks = list(range(6, 10 + 1)) + list('JQKA')
_suits = {
    'spades': '\u2660',
    'hearts': '\u2665',
    'diamonds': '\u2666',
    'clubs': '\u2663'
}

class SuitEnum(Enum):

    def __str__(cls):
        return cls.value


Suit = SuitEnum('Suit', _suits)


class Card:
    __slots__ = 'rank', 'suit'  # consume less memory

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return str(self.rank) + " " + str(self.suit)

## ranks = [6, 7, 8, 9, 10]
## suits = ['clubs', 'spades', 'hearts', 'diamonds']
## itertools.product(ranks, suits)
# equivalent to:
##for r in ranks:
##    for s in suits:
##        print(f'{r} : {s}')


class CardDeckBase:

    def __init__(self):
        self.cards = []
        for rank in _ranks:
            for suit in (Suit):
                self.cards.append(Card(rank,suit))
      
    
    def __str__(self):
       return_string = ""
       for card in self.cards:
            return_string += str(card) + "\n"
       return return_string   


class FrenchDeck(CardDeckBase):
    ...


if __name__ == '__main__':
    ...
