# The frame displaying the finance data evolution

from PyQt5.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QFrame,
    QLabel
)

import Views.v2210_Graphs_Factory as Graphs_Factory
import Views.vh1001_View_Styles as vh 

class View_Graphs():
    def __init__(self, widget:QWidget, parent=None):

        # Members:
        # global_vertical_layout
        # top_graph_widget
        #

        # Layout - initialization
        self.global_vertical_layout = QVBoxLayout(widget)
        vh.medium_margin_layout_style(self.global_vertical_layout)

        # Top graph - initialization
        self.top_graph_widget = QWidget()
        self._create_top_graph()
        #self.global_vertical_layout.addWidget(self._create_top_graph())


        # Bottom section (graph, stats)
        bottom_horizontal_layout_frame = QFrame()
        vh.neutral_widget_style(bottom_horizontal_layout_frame); 
        vh.medium_round_widget_corners(bottom_horizontal_layout_frame)
        vh.set_bkg_color_graphic_widget_style(bottom_horizontal_layout_frame)
        bottom_horizontal_layout = QHBoxLayout()
        bottom_horizontal_layout_frame.setLayout(bottom_horizontal_layout)
        self.global_vertical_layout.addWidget(bottom_horizontal_layout_frame)

        # Graph
        canvas = Graphs_Factory.Month_Expense_Graph("Pie graph")
        bottom_horizontal_layout.addWidget(canvas)
        
        bottom_right_vertical_layout_frame = QFrame()
        bottom_right_vertical_layout = QVBoxLayout()
        bottom_right_vertical_layout_frame.setLayout(bottom_right_vertical_layout)
        for i in range(0,4):
            label = QLabel("Test"+str(i))
            bottom_right_vertical_layout.addWidget(label)
        bottom_horizontal_layout.addWidget(bottom_right_vertical_layout_frame)
    

    def _create_top_graph(self, expense_evolution:dict={} ):
        wnew = QWidget(); 
        self.global_vertical_layout.addWidget(wnew)
        vh.neutral_widget_style(wnew); 
        vh.medium_round_widget_corners(wnew)
        vh.set_bkg_color_graphic_widget_style(wnew)
        top_graph_layout = QHBoxLayout();

        canvas = Graphs_Factory.View_Expense_Evolution_Graph("Expense evolution",expense_evolution)
        top_graph_layout.addWidget(canvas)
        wnew.setLayout(top_graph_layout)
        self.global_vertical_layout.replaceWidget(self.top_graph_widget, wnew)
        self.top_graph_widget = wnew

    def update_expense_evolution_graph(self, expense_evolution:dict={}):
        self._create_top_graph(expense_evolution)



