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

        # Private members:
        # __global_vertical_layout
        # __top_graph_widget
        #

        # Layout - initialization
        self.__global_vertical_layout = QVBoxLayout(widget)
        vh.medium_margin_layout_style(self.__global_vertical_layout)

        # Top graph - initialization
        self.__top_graph_widget = QWidget()
        self._create_top_graph()

        # Bottom section (graph, stats)
        self.__bottom_graph_widget = QFrame()
        self._create_bottom_graph()    

    # A scatter chart view of the expense evolution through month
    def _create_top_graph(self, expense_evolution:dict={} ):
        # Create the new widget for the updated graph
        wnew = QWidget(); 
        vh.neutral_widget_style(wnew); 
        vh.medium_round_widget_corners(wnew)
        vh.set_bkg_color_graphic_widget_style(wnew)
        # Create a layout
        top_graph_layout = QHBoxLayout();
        # Create the graph and add it to the widget
        canvas = Graphs_Factory.View_Expense_Evolution_Graph("Expense evolution",expense_evolution)
        top_graph_layout.addWidget(canvas)
        wnew.setLayout(top_graph_layout)
        # Delete existing graph
        self.__top_graph_widget.setParent(None)
        # Insert the new graph at the top (idx=0)
        self.__global_vertical_layout.insertWidget(0, wnew)
        # Set the new graph as member of the class (for accessibility)
        self.__top_graph_widget = wnew

    # Create the top graph of the graphs view
    def update_expense_evolution_graph(self, expense_evolution:dict={}):
        self._create_top_graph(expense_evolution)

    # A pie chart view of the expense distribution for a selected month
    # expense_distribution:dict --> { CATEGORY : XX% of monthly cost }
    def _create_bottom_graph(self, expense_distribution:dict={}, plot_title="" ):
        #
        wnew = QFrame()
        vh.neutral_widget_style(wnew); 
        vh.medium_round_widget_corners(wnew)
        vh.set_bkg_color_graphic_widget_style(wnew)
        #
        bottom_horizontal_layout = QHBoxLayout()
        #
        canvas = Graphs_Factory.Month_Expense_Graph(plot_title,expense_distribution)
        bottom_horizontal_layout.addWidget(canvas)
        wnew.setLayout(bottom_horizontal_layout)
        #
        self.__bottom_graph_widget.setParent(None)
        # Insert the new graph at the top (idx=0)
        self.__global_vertical_layout.insertWidget(1, wnew)
        # Set the new graph as member of the class (for accessibility)
        self.__bottom_graph_widget = wnew

        #
        
        # bottom_right_vertical_layout_frame = QFrame()
        # bottom_right_vertical_layout = QVBoxLayout()
        # bottom_right_vertical_layout_frame.setLayout(bottom_right_vertical_layout)
        # for i in range(0,4):
        #     label = QLabel("Test"+str(i))
        #     bottom_right_vertical_layout.addWidget(label)
        # self.bottom_horizontal_layout.addWidget(bottom_right_vertical_layout_frame)

      #  canvas = Graphs_Factory.Month_Expense_Graph("Pie graph",expense_distribution)
        #wnew = QWidget(); 
        #vh.neutral_widget_style(wnew); 
        #vh.medium_round_widget_corners(wnew)
        #vh.set_bkg_color_graphic_widget_style(wnew)
        ## Create a layout
        #top_graph_layout = QHBoxLayout();
        ## Create the graph and add it to the widget
        #canvas = Graphs_Factory.View_Expense_Evolution_Graph("Expense evolution",expense_evolution)
        #top_graph_layout.addWidget(canvas)
        #wnew.setLayout(top_graph_layout)
        ## Delete existing graph
        #self.__top_graph_widget.setParent(None)
        ## Insert the new graph at the top (idx=0)
        #self.__global_vertical_layout.insertWidget(0, wnew)
        ## Set the new graph as member of the class (for accessibility)
        #self.__top_graph_widget = wnew



    # Create the bottom graph of the graphs view
    # expense_distribution:dict --> { CATEGORY : XX% of monthly cost }
    def update_expense_distribution_graph(self, expense_distribution:dict={}, plot_title=""):
        self._create_bottom_graph(expense_distribution, plot_title)

