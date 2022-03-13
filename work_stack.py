from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from stack_base import StackBase
import consts

class WorkStack(StackBase):
    def __init__(self, parent):
        super(WorkStack, self).__init__()
        self.parent = parent
        self.setRect(QRectF(consts.CARD_SILO))

    def update(self):
        cur_pos = self.scenePos()
        if len(self.cards) > 0:
            for idx, card in enumerate(self.cards):
                cur_x = cur_pos.x()
                cur_y = cur_pos.y()
                off_x = consts.STACK_OFFSET_X
                off_y = consts.STACK_OFFSET_Y + (idx * 15)
                self.cards[idx].setPos(QPointF(cur_x + off_x, cur_y + off_y))
                self.cards[idx].setZValue(idx)
                # Make sure the top card is always flipped up
                if idx == len(self.cards) - 1:
                    self.cards[idx].flip_up()


    def set_cards(self, deck, num_to_draw):
        cur_drawn_idx = 0
        while cur_drawn_idx < num_to_draw:
            card = deck.give_top_card()
            if card is None:
                print('ERROR: Deck returned None!')
                return
            else:
                card.flip_down()
                card.set_stack(self)
                self.cards.append(card)
            cur_drawn_idx += 1

        self.update()
        for card in self.cards:
            self.parent.scene.addItem(card)
            card.show()

    def accept_card(self, card):
        # A draw pile only gets can get cards from the draw stack
        return True