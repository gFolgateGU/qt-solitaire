from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import os
import stack_base
import draw_stack
import draw_pile
import win_stack
import work_stack
import consts

class Card(QGraphicsPixmapItem):  
    def __init__(self, suit, value, parent_stack = None):
        super(Card, self).__init__()
        self.suit = suit
        self.value = value
        self.stack = parent_stack
        self.face_up = False
        self.children = []
        self.determine_color()
        self.init_properties()
        self.load_image()

    def determine_color(self):
        if self.suit == 'H' or self.suit == 'D':
            self.color_is_red = True
        else:
            self.color_is_red = False
 
    def set_stack(self, parent_stack):
        self.stack = parent_stack

    def init_properties(self):
        self.setShapeMode(QGraphicsPixmapItem.BoundingRectShape)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
        if isinstance(self.stack, draw_stack.DrawStack):
            self.setFlag(QGraphicsItem.ItemIsMovable, False)
        else:
            self.setFlag(QGraphicsItem.ItemIsMovable, True)

    def load_image(self):
        face = QPixmap(os.path.join('assets/cards', '%s%s.png' % (self.value, self.suit)))
        back = QPixmap(os.path.join('assets/cards', 'back.png'))
        self.face = face
        self.back = back
        if self.face_up:
            self.setPixmap(self.face)
        else:
            self.setPixmap(self.back)

    def is_face_up(self):
        return self.face_up

    def flip_up(self):
        # Flip the card up, make movable, and reload image
        self.face_up = True
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.load_image()

    def flip_down(self):
        # Flip the card down, make immovable, and reload image
        self.face_up = False
        self.setFlag(QGraphicsItem.ItemIsMovable, False)
        self.load_image()

    def has_children(self):
        return len(self.children) > 0

    def mouseMoveEvent(self, event):
        """This method modifies the card visibility when dragged"""
        # Set to a very high z value
        high_z = 100
        self.setZValue(high_z)
        cur_pos = self.scenePos()
        for idx, child in enumerate(self.children):
            cur_x = cur_pos.x()
            cur_y = cur_pos.y()
            off_x = consts.WORK_STACK_OFFSET_X
            off_y = (idx + 1) * consts.WORK_STACK_OFFSET_Y
            child.setPos(QPointF(cur_x + off_x, cur_y + off_y))
            child.setZValue(high_z + (idx + 1))

        # Call super class mouse press event
        return super(Card, self).mouseMoveEvent(event)    

    def mouseDoubleClickEvent(self, event):
        items = self.collidingItems()
        if items is not None:
            for item in items:
                if (isinstance(item, draw_stack.DrawStack)):
                    if self.stack == item:
                        item.draw_card(self)
        # Call super class mouse double click event
        return super(Card, self).mouseDoubleClickEvent(event)

    def mouseReleaseEvent(self, event):
        items = self.collidingItems()
        if len(items) > 0:
            for item in items:
                if isinstance(item, win_stack.WinStack) \
                or isinstance(item, work_stack.WorkStack):
                    if self.stack == item:
                        # Just keep it in the same stack
                        break
                    else:
                        accept = item.accept_card(self)
                        if accept:
                            item.add_card(self)
                else:
                    pass
        # Update the stack for any graphics changes   
        self.stack.update()
        # Call super class mouse release event
        return super(Card, self).mouseReleaseEvent(event)