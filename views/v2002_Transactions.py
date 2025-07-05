# The view of the months list

from PyQt5.QtWidgets import (
    QVBoxLayout,
    QLabel
)

class View_Transactions(QVBoxLayout):
    def __init__(self, transactions:list =[] , parent=None):
        super().__init__(parent)

        self.setSpacing(3)
        self.setContentsMargins(5, 5, 5, 5)

        if len(transactions)==0:
            label = QLabel("No month selected")
            label.setStyleSheet("border: 0px; margin: 5px")
            self.addWidget(label)
        else:
            for transaction in transactions:
                label = QLabel(transaction[0]+":  "+str(transaction[1]))
                label.setStyleSheet("border: 0px; margin: 5px")
                self.addWidget(label)

        self.addStretch()



