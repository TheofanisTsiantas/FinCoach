# The frame displaying the finance data evolution

from PyQt5.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QLabel,
    QPushButton,
)

IMPORT_BUTTON_STYLE = """ QPushButton { background-color: #e8d8ac; border-radius: 8px;padding:5px; border: 1px solid grey; }"""


class W_Months_Column(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet("border: 1px solid black;")

        vertical_layout = QVBoxLayout(self)
        
        month_import = QPushButton("Import .csv")
        month_import.setStyleSheet(IMPORT_BUTTON_STYLE)
        vertical_layout.addWidget(month_import)

        label = QLabel("January 1999")
        vertical_layout.addWidget(label)