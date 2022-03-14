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
                off_y = consts.STACK_OFFSET_Y + (idx * consts.WORK_STACK_OFFSET_Y)
                self.cards[idx].setPos(QPointF(cur_x + off_x, cur_y + off_y))
                self.cards[idx].setZValue(idx)
                if self.cards[idx].is_face_up():
                    self.cards[idx].children = self.cards[idx+1::]
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
        """This method lists the rules for which cards are allowed."""
        if self._is_empty_work_stack():
            if self._is_a_king(card):
                return True
            else:
                return False
        else:
            return self._is_in_order(card)

    def _is_empty_work_stack(self):
        if len(self.cards) < 1:
            return True
        return False
        
    def _is_a_king(self, card):
        king_value = 13
        if int(card.value) == king_value:
            return True
        return False

    def _is_in_order(self, card):
        top = self.cards[len(self.cards)-1]
        # First make sure it is the right color
        if top.color_is_red != card.color_is_red:
            # Now ensure the delta rank is +1
            delta_rank = int(top.value) - int(card.value)
            if delta_rank == 1:
                return True
            else:
                return False
        else:
            # Can't add cards of the same color
            return False 

    def add_card(self, card):
        # Get all that card's children
        children = card.children
        # Save off old card information
        old_card_idx = card.stack.cards.index(card)
        old_stack = card.stack
        # Move that card to this stack
        self.cards.append(card.stack.cards[old_card_idx])
        card.stack.cards.remove(card.stack.cards[old_card_idx])
        self.cards[len(self.cards)-1].stack = self.stack
        # Now move all of it's children
        for child in children:
            # Save off old child information
            child_idx = child.stack.cards.index(child)
            # Move the card to the right stack
            self.cards.append(child.stack.cards[child_idx])
            child.stack.cards.remove(child.stack.cards[child_idx])
            self.cards[len(self.cards)-1].stack = self.stack
        self.update()
        old_stack.update()