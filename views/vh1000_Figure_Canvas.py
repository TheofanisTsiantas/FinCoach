# A helper class of the view facilitating in placing a figure in a canvas

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from Views.vh1001_View_Styles import GRAPHICS_BKG_COLOR 

import matplotlib.pyplot as plt


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure(facecolor=GRAPHICS_BKG_COLOR)
        self.axes = self.fig.add_subplot(111) 
        super().__init__(self.fig)


