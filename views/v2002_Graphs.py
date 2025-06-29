# The frame displaying the finance data evolution

from PyQt5.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QFrame,
    QLabel
)

from Views.vh1000_Figure_Canvas import MplCanvas

IMPORT_BUTTON_STYLE = """ QPushButton { background-color: #e8d8ac; border-radius: 8px;padding:5px; border: 1px solid grey; }"""

class View_Graphs(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Outer border
        self.setStyleSheet("border: 1px solid black;")
        # Widget layout
        global_vertical_layout = QVBoxLayout(self)
        # Top graph
        canvas = MplCanvas(self)
        canvas.axes.plot([0, 1, 2, 3], [10, 1, 20, 3])
        global_vertical_layout.addWidget(canvas)
        # Bottom section (graph, stats)
        bottom_horizontal_layout_frame = QFrame()
        bottom_horizontal_layout = QHBoxLayout()
        bottom_horizontal_layout_frame.setLayout(bottom_horizontal_layout)
        global_vertical_layout.addWidget(bottom_horizontal_layout_frame)
        # Graph
        canvas = MplCanvas(self)
        canvas.axes.plot([0, 1, 2, 3], [10, 1, 20, 3], color='red')
        bottom_horizontal_layout.addWidget(canvas)
        
        bottom_right_vertical_layout_frame = QFrame()
        bottom_right_vertical_layout = QVBoxLayout()
        bottom_right_vertical_layout_frame.setLayout(bottom_right_vertical_layout)
        for i in range(0,4):
            label = QLabel("Test"+str(i))
            bottom_right_vertical_layout.addWidget(label)
        bottom_horizontal_layout.addWidget(bottom_right_vertical_layout_frame)




