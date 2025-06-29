# The frame displaying the finance data evolution

from PyQt5.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QLabel
)

from Views.v2001_Months import View_Months
from Views.v2002_Graphs import View_Graphs

IMPORT_BUTTON_STYLE = """ QPushButton { background-color: #e8d8ac; border-radius: 8px;padding:5px; border: 1px solid grey; }"""


class W_Main_Frame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFrameShape(QFrame.Panel)
        self.setStyleSheet("border: 1px solid black; background-color: #eeeeee;")

        main_frame_layout = QHBoxLayout()
        main_frame_layout.setContentsMargins(5, 5, 5, 5)
        self.setLayout(main_frame_layout)

        # --- Months
        self.months_menu = View_Months(self)
        main_frame_layout.addWidget(self.months_menu,1)

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




##        label = QLabel("This is the Main Frame")
##        layout.addWidget(label)
