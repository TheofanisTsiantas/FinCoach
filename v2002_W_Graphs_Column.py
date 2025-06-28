# The frame displaying the finance data evolution

from PyQt5.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QLabel,
    QPushButton,
)

IMPORT_BUTTON_STYLE = """ QPushButton { background-color: #e8d8ac; border-radius: 8px;padding:5px; border: 1px solid grey; }"""

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure()
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class W_Graphs_Column(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet("border: 1px solid black;")

        vertical_layout = QVBoxLayout(self)

        label = QLabel("My graphs")
        vertical_layout.addWidget(label)

        canvas = MplCanvas(self)
        canvas.axes.plot([0, 1, 2, 3], [10, 1, 20, 3])

        vertical_layout.addWidget(canvas)

        label = QLabel("My graphs2 ")
        vertical_layout.addWidget(label)

        canvas = MplCanvas(self)
        canvas.axes.plot([0, 1, 2, 3], [10, 1, 20, 3])

        vertical_layout.addWidget(canvas)


