from Pyside6.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout
from Pyside6.QtGui import QFont
from PySide6.QtCore import Qt



class Interface_application(QtWidget):

    def __init__(self):
        super.__init__()

        self.Horoscope = QLabel("Horoscope")
        self.FunFact = QLabel("Fun Fact")
        self.Camera = QLabel("Caméra")
        self.Pluie = QPushButton("Pluie")
        self.Pression = QPushButton("Pression")
        self.soleil = QPushButton("Soleil")
        self.Vent = QPushButton("Vent")
