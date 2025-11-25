# The view of the months list

from datetime import datetime
from PyQt5.QtWidgets import (
    QVBoxLayout,
    QLabel
)

from PyQt5.QtCore import pyqtSignal

from typing import TYPE_CHECKING, Callable, Optional
from functools import partial

if TYPE_CHECKING:
    from Controllers.c1001_Main_Frame import Controller_Main_Frame

class View_Months(QVBoxLayout):
    def __init__(self, months:list =[] , callback:Optional[Callable]=None,  parent=None):
        super().__init__(parent)

        self.setSpacing(3)
        self.setContentsMargins(5, 5, 5, 5)
        self.labels: list[QLabel] = []

        if months is None or len(months)==0:
            label = QLabel("No months read")
            label.setStyleSheet("border: 0px; margin: 5px")
            self.addWidget(label)
        else:
            month_dt = [datetime.strptime(month, "%m-%Y") for month in months]
            sorted_month_dt = sorted(month_dt); #.dt.month.astype(str) + "-" + df['Date'].dt.year.astype(str)
            sorted_months = [str(dt.month)+"-"+str(dt.year) for dt in sorted_month_dt]
            for month in sorted_months:
                label = ClickableLabel(month)
                label.setEnabled(True)
                label.setStyleSheet("border: 0px; margin: 5px")
                self.addWidget(label)
                self.labels.append(label)
                label.clicked.connect(partial(self._label_clicked, label.text(), callback))

        self.addStretch()

    # Private method to handle the view logic
    def _label_clicked(self, month:str, callback:Optional[Callable]=None ):
        # Remove any existing background (from previous selections)
        for label in self.labels:
            label.setStyleSheet("background-color: white; color: black; border: 0px; margin: 5px")
        # Call parent view - month has been selected
        callback(month)

class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        # Remove background
        self.clicked.emit()
        # Set backround of the current one to blue
        self.setStyleSheet("background-color: rgb(47, 117, 250); color: white; border: 0px; border-radius:5px; margin: 5px")
        # Default functionality fallback
        super().mousePressEvent(event)
