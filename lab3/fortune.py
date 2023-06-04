from cards import *
from cards import _ranks

import random

class Prediction:
    def __init__(self, part_1, verb, adjective, part_2, object):
        self.prediction = str(part_1) + " " + str(verb) +  " " + str(adjective) + " " + str(part_2) + " " + str(object)
    
    def __str__(self):
        return str(self.prediction)

class PredictionsSet:
    def __init__(self, suit, part_1, positive_verb, negative_verb, *adjective_set, part_2, object):
        self.suit = suit
        self.predictions = []
        for i in range(9):
            verb =  negative_verb if i < 4 else positive_verb
            self.predictions.append(Prediction(part_1, verb, adjective_set[i], part_2, object))
        


class Fortune:
    
    adjective_set = ["abysmal", "terrible", "awful", "bad", "fair", "fine", "good", "great", "incredible"]

    dimonds_predictions = PredictionsSet(Suit.diamonds, "You will", "get", "lost", *adjective_set, part_2="amount of",object="money")
    hearts_predictions = PredictionsSet(Suit.hearts, "You will", "feel", "feel", *adjective_set, part_2="",object="")
    clubs_predictions = PredictionsSet(Suit.clubs, "You will", "meet", "struggle with", *adjective_set, part_2="",object="luck")
    spades_predictions = PredictionsSet(Suit.spades, "You will", "feel", "be heartbroken with", *adjective_set, part_2="",object="love")

    reset_value = -100

    diamond_value = reset_value
    hearts_value = reset_value
    clubs_value = reset_value
    spades_value = reset_value


    def __init__(self, min_card_amount, max_card_amount):
        self.deck = CardDeckBase()
        random.seed()
        self.cards_amount = random.randrange(min_card_amount, max_card_amount, 1)
        self.dealt_cards = []

    def deal_cards(self):
        random.shuffle(self.deck.cards)
        for i in range(self.cards_amount):
            self.dealt_cards.append(self.deck.cards[i])

    def print_dealt_cards(self):
        for card in self.dealt_cards:
            print(card)
    
    def calc_ranks(self):
        self.diamond_value = self.reset_value
        self.hearts_value = self.reset_value
        self.clubs_value = self.reset_value
        self.spades_value = self.reset_value
        for i in range(self.cards_amount):
            temp = _ranks.index(self.dealt_cards[i].rank)
            # Normalise ranks
            if(temp <= 3):
                temp = (3 - temp) * -1
            else:
                temp = temp - 3

                if elf.dealt_cards[i].suit.name = 'spades':
                    if(self.spades_value == self.reset_value):
                        self.spades_value = 3
                    self.spades_value = self.spades_value +  temp
                elif elf.dealt_cards[i].suit.name = 'hearts':
                    if(self.hearts_value == self.reset_value):
                        self.hearts_value = 3
                    self.hearts_value = self.hearts_value +  temp
                elif elf.dealt_cards[i].suit.name = 'diamonds':
                    if(self.diamond_value == self.reset_value):
                        self.diamond_value = 3
                    self.diamond_value = self.diamond_value +  temp
                elif elf.dealt_cards[i].suit.name = 'clubs':
                    if(self.clubs_value == self.reset_value):
                        self.clubs_value = 3
                    self.clubs_value = self.clubs_value +  temp
                
    def clamp_ranks(self):
        if(self.spades_value > 8):
            self.spades_value = 8
        if(self.hearts_value > 8):
            self.hearts_value = 8
        if(self.diamond_value > 8):
            self.diamond_value = 8
        if(self.clubs_value > 8):
            self.clubs_value = 8

    def provide_message(self):
        if(self.spades_value != self.reset_value):
            print(self.spades_predictions.predictions[self.spades_value])
        if(self.hearts_value != self.reset_value):
            print(self.hearts_predictions.predictions[self.spades_value])
        if(self.diamond_value != self.reset_value):
            print(self.dimonds_predictions.predictions[self.spades_value])
        if(self.clubs_value != self.reset_value):
            print(self.clubs_predictions.predictions[self.spades_value])      
     

fortune = Fortune(4,6)
fortune.deal_cards()
fortune.print_dealt_cards()
print("----------- Translating into prediction -----------")
fortune.calc_ranks()
fortune.clamp_ranks()
fortune.provide_message()





