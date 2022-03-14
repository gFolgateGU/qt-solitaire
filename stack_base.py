from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import consts

class StackBase(QGraphicsRectItem):
    def __init__(self):
        super(StackBase, self).__init__()
        self.setRect(QRectF(consts.CARD_SILO))
        self.stack = self
        self.cards = []

    def update(self):
        raise NotImplementedError()

    def accept_card(self, card):
        raise NotImplementedError()

    def clear_cards(self):
        #for card in self.cards:
            #card.children.clear()
        self.cards.clear()

    def add_card(self, card):
        # Remove the card from its old stack and add it to its new stack
        self.cards.append(card.stack.cards.pop())
        # Make sure the cards new stack refers to this stack
        old_stack = self.cards[len(self.cards)-1].stack
        self.cards[len(self.cards)-1].stack = self.stack
        # Make any graphical changes to the interface
        self.update()
        old_stack.update()