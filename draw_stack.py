from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from stack_base import StackBase
from card import Card
import consts

class DrawStack(StackBase):
    def __init__(self, parent):
        super(DrawStack, self).__init__()
        self.parent = parent
        self.setRect(QRectF(consts.CARD_SILO))

    def update(self):
        cur_pos = self.scenePos()
        if len(self.cards) > 0:
            for idx, card in enumerate(self.cards):
                cur_x = cur_pos.x()
                cur_y = cur_pos.y()
                off_x = consts.STACK_OFFSET_X
                off_y = consts.STACK_OFFSET_X
                self.cards[idx].setPos(QPointF(cur_x + off_x, cur_y + off_y))
                self.cards[idx].setZValue(idx)

    def accept_card(self, card):
        # A draw stack will never take cards
        # The only way a draw stack can get cards
        # is if draw stack recycle is hit
        return False

    def draw_card(self, card):
        if len(self.cards) > 0:
            if card == self.cards[-1]:
                card.flip_up()
                self.parent.draw_pile.add_card(card)

    def show_card(self):
        my_card = Card('D', '4', self)
        my_card2 = Card('C', '7', self)
        cur_pos = self.scenePos()
        self.cards.append(my_card)
        self.cards.append(my_card2)
        self.update()
        self.parent.scene.addItem(self.cards[0])
        self.parent.scene.addItem(self.cards[1])
        self.cards[0].show()
        self.cards[1].show()

    def mouseDoubleClickEvent(self, event):
        """This method draws the top card or recycles the draw pile back to the draw stack"""
        if len(self.cards) > 0:
            self.draw_card(self.cards[-1])
        else:
            # This is the case where all of the cards need to be recycle from draw pile
            self._recycle_cards()

    def _recycle_cards(self):
        """This method takes all of the cards from the draw pile back to draw stack"""
        draw_pile_cards = self.parent.draw_pile.cards
        while len(draw_pile_cards) > 0:
            draw_pile_cards[-1].flip_down()
            self.add_card(draw_pile_cards[-1])