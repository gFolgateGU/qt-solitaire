import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QtSolitaireWindow(QWidget):
    def __init__(self, parent=None):
        super(QtSolitaireWindow, self).__init__(parent)
        self.resize(800, 600)
        self.setWindowTitle('QtSolitaire')
        self.setStyleSheet("background-color:green")
        self.label = QLabel(self)
        self.label.setText('Lets play solitaire')
        self.label.move(50, 20)


if __name__ == '__main__':
    solitaire_app = QApplication(sys.argv)
    solitaire_gui = QtSolitaireWindow()
    solitaire_gui.show()
    sys.exit(solitaire_app.exec())
