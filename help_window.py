from PyQt5.QtWidgets import *


class HelpWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Help Menu")
        self.resize(200, 200)