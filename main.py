import sys
from turtle import onclick
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from help_window import HelpWindow
from game_board import GameBoard

class QtSolitaireWindow(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer for the main application"""
        super().__init__(parent)
        self.setWindowTitle("QtSolitaire")

        # Create the game board
        self._create_game_board()

        # Create the main menu bar
        self._create_menu_bar()

    def _create_menu_bar(self):
        """Create top level game controls"""
        menu_bar = self.menuBar()
 
        # Creating main game controls menu
        game_menu = QMenu("&Game Controls", self)       
        new_game = QAction("&New Game", self)
        new_game.triggered.connect(self.start_new_game)
        quit_game = QAction("&Quit Game", self)
        quit_game.triggered.connect(self.quit_game)       
        game_menu.addAction(new_game)
        game_menu.addAction(quit_game)
        menu_bar.addMenu(game_menu)

        # Create help menu
        help_menu = QAction("&Help", self)
        help_menu.triggered.connect(self.show_help_dialog)
        menu_bar.addAction(help_menu)
        
        menu_bar.setNativeMenuBar(False)
        self.setMenuBar(menu_bar)

    def _create_game_board(self):
        """Create the main game board that holds card and stacks"""
        self.game_board = GameBoard(self)

    def start_new_game(self):
        """Start a new game after a completion or stop."""
        self.game_board.start_new_game()

    def quit_game(self):
        """Quit the application"""
        sys.exit()

    def show_help_dialog(self):
        """Show help dialog for instructions on how to play"""
        self._help_window = HelpWindow()
        self._help_window.show()

if __name__ == '__main__':
    solitaire_app = QApplication(sys.argv)
    solitaire_gui = QtSolitaireWindow()
    solitaire_gui.show()
    solitaire_app.exec()
