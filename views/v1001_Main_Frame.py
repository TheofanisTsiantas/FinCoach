# The frame displaying the finance data evolution

from PyQt5.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QLabel,
    QPushButton,
    QFileDialog
)

from PyQt5.QtCore import pyqtSlot
from typing import TYPE_CHECKING

#
from Views.v2001_Months import View_Months
from Views.v2002_Graphs import View_Graphs

#
if TYPE_CHECKING:
    from Controllers.c1001_Main_Frame import Controller_Main_Frame

IMPORT_BUTTON_STYLE = """ QPushButton { background-color: #e8d8ac; border-radius: 8px;padding:5px; border: 1px solid grey; }"""

class View_Main_Frame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialize control object with null. It is assigned by controller 
        self.controlObject : Controller_Main_Frame = None

        self.setFrameShape(QFrame.Box)
        self.setStyleSheet("border: 1px solid black; background-color: #eeeeee;")

        main_frame_layout = QHBoxLayout()
        main_frame_layout.setContentsMargins(5, 5, 5, 5)
        self.setLayout(main_frame_layout)

        # --- Months
        vertical_frame = QWidget(self)
        vertical_frame.setStyleSheet("border: 0.5px solid black;")
        vertical_layout = QVBoxLayout(vertical_frame)
        # Import button
        month_import = QPushButton("Import .csv")
        month_import.setStyleSheet(IMPORT_BUTTON_STYLE)
        month_import.clicked.connect(self._importCSV)
        vertical_layout.addWidget(month_import)
        # View of months
        months_frame = QWidget()
        months_frame.setStyleSheet("background-color:white; border: 1px solid green;")
        months_layout = View_Months()
        months_frame.setLayout(months_layout)
        vertical_layout.addWidget(months_frame,1)
        main_frame_layout.addWidget(vertical_frame,1)

        # --- Graphs
        self.graphs_menu = View_Graphs(self)
        main_frame_layout.addWidget(self.graphs_menu,4)

        # --- Info
        info_menu = QWidget()
        info_menu.setStyleSheet("border: 1px solid black;")
        info_VL = QVBoxLayout(info_menu)
        label = QLabel("Details")
        info_VL.addWidget(label)

        # main_frame_layout.addWidget(info_menu)
        main_frame_layout.addWidget(info_menu,2)

    @pyqtSlot()
    def _importCSV(self):
        # Open the file dialog
        file_name, _ = QFileDialog.getOpenFileName(
        self,                          # parent
        "Select CSV file",             # dialog title
        "",                            # initial directory
        "CSV Files (*.csv);;"#           ;All Files (*)" 
        )
        if file_name and self.controlObject:
            self.controlObject.test()
            # print("Selected file:", file_name)
            # TODO: Do something with the file (e.g., load data)
