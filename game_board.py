from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from draw_stack import DrawStack
from draw_pile import DrawPile
from win_stack import WinStack
from work_stack import WorkStack
from deck import Deck

class GameBoard():
    """
    Container of the game and its components 
    """
    def __init__(self, parent):
        """
        Default constructor of the Gameboard class
        """
        self.parent = parent
        self.win_stacks = []
        self.work_stacks = []
        self.draw_pile = []
        self.draw_stack = []
        self.start_new_game()

    def start_new_game(self):
        """
        Method to start a new solitaire game.
        """
        # Clear all the stacks (if applicable)
        self._clear_stacks()
        # Re-initialize the scene
        self._init_scene()
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

    def _init_scene(self):
        """
        Initialize the gameboard graphics and add to parent main app
        """
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(QRectF(0, 0, 800, 600))
        self.view = QGraphicsView(self.scene)
        self.view.setStyleSheet("background-color:green")
        self.parent.setCentralWidget(self.view)

    def _clear_stacks(self):
        """
        Clear any card stacks that have been set during gameplay
        """
        for win_stack in self.win_stacks:
            win_stack.clear_cards()
        for work_stack in self.work_stacks:
            work_stack.clear_cards()
        if isinstance(self.draw_pile, DrawPile):
            self.draw_pile.clear_cards()
        if isinstance(self.draw_stack, DrawStack):
            self.draw_stack.clear_cards()

    def _init_deck(self):
        """
        Initialize and shuffle the playing card deck
        """
        self.deck = Deck()
        self.deck.shuffle_cards()

    def _init_win_stacks(self):
        """
        Initialize the stacks used to win the game
        """
        num_win_stacks = 4
        self.win_stacks = []
        for idx in range(num_win_stacks):
            win_stack = WinStack(self)
            win_stack.setPos(50 + (idx * 100), 25)
            self.scene.addItem(win_stack)
            win_stack.show()
            self.win_stacks.append(win_stack)

    def _init_work_stacks(self):
        """
        Initialize the stacks used to build off of and help win the game
        """
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
        """
        Initialize the draw stack to pull cards from to help build work stacks
        and win stacks.
        """
        self.draw_stack = DrawStack(self)
        self.draw_stack.setPos(650, 25)
        self.draw_stack.set_cards(self.deck)
        self.scene.addItem(self.draw_stack)
        self.draw_stack.show()

    def _init_draw_pile(self):
        """
        Initialize the draw pile that cards from the draw stack are placed
        """
        self.draw_pile = DrawPile(self)
        self.draw_pile.setPos(550, 25)
        self.scene.addItem(self.draw_pile)
        self.draw_pile.show()