# The view of the months list

from PyQt5.QtWidgets import (
    QVBoxLayout,
    QLabel
)

class View_Months(QVBoxLayout):
    def __init__(self, months:list =[] , parent=None):
        super().__init__(parent)

        self.setSpacing(3)
        self.setContentsMargins(5, 5, 5, 5)
        
        if not months:
            label = QLabel("No months read")
            label.setStyleSheet("border: 0px")
            self.addWidget(label)
        else:
            for month in months:
                label = QLabel(month)
                label.setStyleSheet("border: 0px")
                self.addWidget(label)

        self.addStretch()



