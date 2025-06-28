# The frame displaying the finance data evolution

from PyQt5.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QLabel,
    QPushButton,
    QFileDialog
)
from PyQt5.QtCore import pyqtSlot


IMPORT_BUTTON_STYLE = """ QPushButton { background-color: #e8d8ac; border-radius: 8px;padding:5px; border: 1px solid grey; }"""

class View_Months(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet("border: 1px solid black;")

        vertical_layout = QVBoxLayout(self)
        
        month_import = QPushButton("Import .csv")
        month_import.setStyleSheet(IMPORT_BUTTON_STYLE)
        # singal
        month_import.clicked.connect(self._importCSV)
        vertical_layout.addWidget(month_import)

        label = QLabel("January 1999")
        vertical_layout.addWidget(label)


    @pyqtSlot()
    def _importCSV(self):
        # Open the file dialog
        file_name, _ = QFileDialog.getOpenFileName(
        self,                          # parent
        "Select CSV file",             # dialog title
        "",                            # initial directory
        "CSV Files (*.csv);;All Files (*)"  # filter
        )
        if file_name:
            print("Selected file:", file_name)
            # TODO: Do something with the file (e.g., load data)
