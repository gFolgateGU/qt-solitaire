from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import os

from draw_stack import DrawStack
from draw_pile import DrawPile

class GameBoard():
    def __init__(self, parent):
        self.parent = parent
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(QRectF(0, 0, 800, 600))
        self.view = QGraphicsView(self.scene)
        self.view.setStyleSheet("background-color:green")
        self.parent.setCentralWidget(self.view)
        # Initialize the draw stack
        self._init_draw_stack()
        # Initialize the draw pile
        self._init_draw_pile()

    def _init_draw_stack(self):
        self.draw_stack = DrawStack(self)
        self.draw_stack.setPos(650, 25)
        self.draw_stack.show_card()
        self.scene.addItem(self.draw_stack)
        self.draw_stack.show()

    def _init_draw_pile(self):
        self.draw_pile = DrawPile()
        self.draw_pile.setPos(550, 25)
        self.scene.addItem(self.draw_pile)
        self.draw_pile.show()

    def start_new_game(self):
        pass