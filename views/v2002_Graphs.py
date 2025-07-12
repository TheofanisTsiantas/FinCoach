# The frame displaying the finance data evolution

from PyQt5.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QFrame,
    QLabel
)

from Views.vh1000_Figure_Canvas import MplCanvas
import Views.vh1001_View_Styles as vh 

class View_Graphs():
    def __init__(self, widget:QWidget, parent=None):

        global_vertical_layout = QVBoxLayout(widget)
        vh.medium_margin_layout_style(global_vertical_layout)

        # Top graph 
        top_graph_widget = QWidget(); 
        vh.neutral_widget_style(top_graph_widget); 
        vh.medium_round_widget_corners(top_graph_widget)
        vh.set_bkg_color_graphic_widget_style(top_graph_widget)
        top_graph_layout = QHBoxLayout();

        canvas = MplCanvas(self)
        canvas.axes.plot([0, 1, 2, 3], [10, 1, 20, 3])

        top_graph_layout.addWidget(canvas)
        top_graph_widget.setLayout(top_graph_layout)
        global_vertical_layout.addWidget(top_graph_widget)


        # Bottom section (graph, stats)
        bottom_horizontal_layout_frame = QFrame()
        vh.neutral_widget_style(bottom_horizontal_layout_frame); 
        vh.medium_round_widget_corners(bottom_horizontal_layout_frame)
        vh.set_bkg_color_graphic_widget_style(bottom_horizontal_layout_frame)
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
    





