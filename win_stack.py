from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from stack_base import StackBase
import consts

class WinStack(StackBase):
    def __init__(self, parent):
        """Default constructor of the WinStack class"""
        super(WinStack, self).__init__()
        self.parent = parent
        self.host_suit = None
        self.top_value = int('0')
        self.setRect(QRectF(consts.CARD_SILO))

    def update(self):
        """This method updates the graphical components of the stack."""
        # First update the stack properties for bookkeeping
        self._update_properties()
        # Now take care of the graphical component
        cur_pos = self.scenePos()
        if len(self.cards) > 0:
            for idx, card in enumerate(self.cards):
                cur_x = cur_pos.x()
                cur_y = cur_pos.y()
                off_x = consts.STACK_OFFSET_X
                off_y = consts.STACK_OFFSET_Y
                self.cards[idx].setPos(QPointF(cur_x + off_x, cur_y + off_y))
                self.cards[idx].setZValue(idx)

    def accept_card(self, card):
        """This method lists the rules for which cards are allowed."""
        if (card.has_children()):
            return False
        else:
            if self._is_proper_suit(card):
                if self._is_in_order(card):
                    return True     
            return False

    def _is_proper_suit(self, card):
        if self.host_suit is None:
            return True
        else:
            if self.host_suit == card.suit:
                return True
        return False

    def _is_in_order(self, card):
        card_value = int(card.value)
        delta_rank = card_value - self.top_value
        if delta_rank == 1:
            return True
        return False

    def _update_properties(self):
        if len(self.cards) < 1:
            self.host_suit = None
            self.top_value = int('0')
        else:
            top_card = self.cards[len(self.cards)-1]
            self.top_value = int(top_card.value)

    def add_card(self, card):
        # If the host suit has not been set, set it now
        if self.host_suit == None:
            self.host_suit = card.suit
        # Update the top value in the stack
        self.top_value = int(card.value)
        # Call super class add card method
        super().add_card(card)