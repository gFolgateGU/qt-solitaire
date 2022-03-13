from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import os
import stack_base
import draw_stack
import draw_pile

class Card(QGraphicsPixmapItem):
    def __init__(self, suit, value, parent_stack):
        super(Card, self).__init__()
        self.suit = suit
        self.value = value
        self.stack = parent_stack
        self.face_up = False
        self.init_properties()
        self.load_image()

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

    def mouseDoubleClickEvent(self, event):
        items = self.collidingItems()
        if items is not None:
            for item in items:
                if (isinstance(item, draw_stack.DrawStack)):
                    if self.stack == item:
                        item.draw_card(self)

    def mouseReleaseEvent(self, event):
        items = self.collidingItems()
        if len(items) > 0:
            for item in items:
                if (isinstance(item, stack_base.StackBase)):
                    if self.stack == item:
                        # Just keep it in the same stack
                        break
                    else:
                        accept = item.accept_card(self)
                        if accept:
                            item.add_card(self)
                else:
                    print('Pending behavior...')
        self.stack.update()
        
        return super(Card, self).mouseReleaseEvent(event)