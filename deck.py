from card import Card

import consts
import random

class Deck:
    def __init__(self):
        self.cards = []
        self._init_cards()

    def print_cards(self):
        for card in self.cards:
            print(f'{card.value} of {card.suit}')

    def shuffle_cards(self):
        num_cards = len(self.cards)
        for idx in range(num_cards):
            rand_idx = random.randint(0, num_cards - 1)
            temp = self.cards[idx]
            self.cards[idx] = self.cards[rand_idx]
            self.cards[rand_idx] = temp

    def give_top_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

    def _init_cards(self):
        """Add all of the cards in the deck to master array"""
        card_suits = consts.CARD_SUITS
        card_vals = consts.CARD_VALUES

        for suit in card_suits:
            for value in card_vals:
                new_card = Card(suit, value)
                self.cards.append(new_card)