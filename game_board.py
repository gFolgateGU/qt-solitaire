from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import os

CARD_RECT = QRect(0, 0, 80, 116)
OFFSET_X = 50
OFFSET_Y = 10
CARD_SPACING = 100


class Card(QGraphicsPixmapItem):
    def __init__(self):
        super(Card, self).__init__()
        self.setShapeMode(QGraphicsPixmapItem.BoundingRectShape)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
        self.load_image()

    def load_image(self):
        print('hiii')
        face = QPixmap(os.path.join('assets/cards', '4D.png'))
        self.setPixmap(face)


class StackBase(QGraphicsRectItem):
    def __init__(self):
        super(StackBase, self).__init__()
        self.setRect(QRectF(CARD_RECT))


class GameBoard():
    def __init__(self, parent):
        self.parent = parent
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(QRectF(0, 0, 800, 600))
        self.view = QGraphicsView(self.scene)
        self.view.setStyleSheet("background-color:green")
        self.parent.setCentralWidget(self.view)

        stack1 = StackBase()
        stack1.setPos(25, 25)
        self.scene.addItem(stack1)

        stack2 = StackBase()
        stack2.setPos(125, 25)
        self.scene.addItem(stack2)

        card = Card()
        card.setPos(200, 200)
        self.scene.addItem(card)
        card.show()


    def start_new_game(self):
        pass