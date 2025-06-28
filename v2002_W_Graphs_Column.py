# The frame displaying the finance data evolution

from PyQt5.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QLabel,
    QPushButton,
)

IMPORT_BUTTON_STYLE = """ QPushButton { background-color: #e8d8ac; border-radius: 8px;padding:5px; border: 1px solid grey; }"""


class W_Graphs_Column(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet("border: 1px solid black;")

        vertical_layout = QVBoxLayout(self)
        label = QLabel("My graphs")
        vertical_layout.addWidget(label)