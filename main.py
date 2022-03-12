import sys
from turtle import onclick
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from help_window import HelpWindow

class QtSolitaireWindow(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("QtSolitaire")
        self.resize(400, 200)
        self.centralWidget = QLabel("Hello, World")
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)
        self.setStyleSheet("background-color:green")
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

    def start_new_game(self):
        # Placeholder functionality to start a new game.
        self.centralWidget.setText('Starting new game...')

    def quit_game(self):
        sys.exit()

    def show_help_dialog(self):
        print('hereee')
        self._help_window = HelpWindow()
        self._help_window.show()

if __name__ == '__main__':
    solitaire_app = QApplication(sys.argv)
    solitaire_gui = QtSolitaireWindow()
    solitaire_gui.show()
    solitaire_app.exec()
