from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import os

from draw_stack import DrawStack
from draw_pile import DrawPile
from win_stack import WinStack
from work_stack import WorkStack
from deck import Deck

class GameBoard():
    def __init__(self, parent):
        self.parent = parent
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(QRectF(0, 0, 800, 600))
        self.view = QGraphicsView(self.scene)
        self.view.setStyleSheet("background-color:green")
        self.parent.setCentralWidget(self.view)
        # Initialize the game deck
        self._init_deck()
        # Initialize the win stacks
        self._init_win_stacks()
        # Initialize the work stacks
        self._init_work_stacks()
        # Initialize the draw stack
        self._init_draw_stack()
        # Initialize the draw pile
        self._init_draw_pile()

    def _init_deck(self):
        self.deck = Deck()
        self.deck.shuffle_cards()

    def _init_win_stacks(self):
        num_win_stacks = 4
        self.win_stacks = []
        for idx in range(num_win_stacks):
            win_stack = WinStack(self)
            win_stack.setPos(50 + (idx * 100), 25)
            self.scene.addItem(win_stack)
            win_stack.show()
            self.win_stacks.append(win_stack)

    def _init_work_stacks(self):
        num_work_stacks = 7
        self.work_stacks = []
        for idx in range(num_work_stacks):
            work_stack = WorkStack(self)
            work_stack.setPos(50 + (idx * 100), 200)
            work_stack.set_cards(self.deck, idx+1)
            self.scene.addItem(work_stack)
            work_stack.show()
            self.work_stacks.append(work_stack)

    def _init_draw_stack(self):
        self.draw_stack = DrawStack(self)
        self.draw_stack.setPos(650, 25)
        self.draw_stack.set_cards(self.deck)
        self.scene.addItem(self.draw_stack)
        self.draw_stack.show()

    def _init_draw_pile(self):
        self.draw_pile = DrawPile(self)
        self.draw_pile.setPos(550, 25)
        self.scene.addItem(self.draw_pile)
        self.draw_pile.show()

    def start_new_game(self):
        pass