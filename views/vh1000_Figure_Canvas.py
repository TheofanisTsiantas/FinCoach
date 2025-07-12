# A helper class of the view facilitating in placing a figure in a canvas

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from Views.vh1001_View_Styles import GRAPHICS_BKG_COLOR 

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure(facecolor=GRAPHICS_BKG_COLOR)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)