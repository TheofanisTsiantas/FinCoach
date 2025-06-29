# The view of the months list

from PyQt5.QtWidgets import (
    QVBoxLayout,
    QLabel
)

class View_Months(QVBoxLayout):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSpacing(3)
        self.setContentsMargins(5, 5, 5, 5)

        label = QLabel("No months read")
        label.setStyleSheet("border: 0px")
        self.addWidget(label)

        self.addStretch()


    def update(self, list_of_months):
        for month in list_of_months:
            print(month)

