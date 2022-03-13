from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from stack_base import StackBase
import consts

class DrawPile(StackBase):
    def __init__(self, parent):
        super(DrawPile, self).__init__()
        self.parent = parent
        self.setRect(QRectF(consts.CARD_SILO))


    def update(self):
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
        # A draw pile only gets can get cards from the draw stack
        return True