# The view of the months list

from PyQt5.QtWidgets import (
    QVBoxLayout,
    QLabel
)

from PyQt5.QtCore import pyqtSignal

class View_Months(QVBoxLayout):
    def __init__(self, months:list =[] , parent=None):
        super().__init__(parent)

        self.setSpacing(3)
        self.setContentsMargins(5, 5, 5, 5)
        self.labels: list[QLabel] = []

        
        if months is None or len(months)==0:
            label = QLabel("No months read")
            label.setStyleSheet("border: 0px; margin: 5px")
            self.addWidget(label)
        else:
            for month in months:
                label = ClickableLabel(month)
                label.setEnabled(True)
                label.setStyleSheet("border: 0px; margin: 5px")
                self.addWidget(label)
                self.labels.append(label)
                label.clicked.connect(self._clean_background)

        self.addStretch()

    # Private method to remove the background of all months (in case one has been selected before)
    def _clean_background(self):
        for label in self.labels:
            label.setStyleSheet("background-color: white; color: black; border: 0px; margin: 5px")

class ClickableLabel(QLabel):
    clicked = pyqtSignal()
    def mousePressEvent(self, event):
        # Remove background
        self.clicked.emit()
        # Set backround of the current one to blue
        self.setStyleSheet("background-color: rgb(47, 117, 250); color: white; border: 0px; border-radius:5px; margin: 5px")
        #

        # Default functionality fallback
        super().mousePressEvent(event)
