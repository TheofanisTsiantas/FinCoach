# The frame displaying the finance data evolution

from PyQt5.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QLabel,
    QPushButton,
    QStyle
)

IMPORT_BUTTON_STYLE = """ QPushButton { background-color: #e8d8ac; border-radius: 8px;padding:5px; border: 1px solid grey; }"""


class Main_Frame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFrameShape(QFrame.Panel)
        self.setStyleSheet("border: 1px solid black; background-color: #eeeeee;")

        main_frame_layout = QHBoxLayout()
        main_frame_layout.setContentsMargins(5, 5, 5, 5)
        self.setLayout(main_frame_layout)

        # ---------- Vertical layouts ----------
        # --- Months
        months_menu = QWidget()
        months_menu.setStyleSheet("border: 1px solid black;")

        months_VL = QVBoxLayout(months_menu)
        
        # Import month button
        month_import = QPushButton("Import .csv")
        month_import.setStyleSheet(IMPORT_BUTTON_STYLE)
        months_VL.addWidget(month_import)

        label = QLabel("January 1999")
        months_VL.addWidget(label)

        main_frame_layout.addWidget(months_menu)
        main_frame_layout.addWidget(months_menu,1)
        
        # --- Graphs
        graphs_menu = QWidget()
        graphs_menu.setStyleSheet("border: 1px solid black;")
        graphs_VL = QVBoxLayout(graphs_menu)
        label = QLabel("My graphs")
        graphs_VL.addWidget(label)

        #main_frame_layout.addWidget(graphs_menu)
        main_frame_layout.addWidget(graphs_menu,4)

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
