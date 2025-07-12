# The frame displaying the finance data evolution

from PyQt5.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QFileDialog,
    QDialog,
    QScrollArea,
    QLabel
)

from PyQt5.QtCore import pyqtSlot
from typing import TYPE_CHECKING

#
from Views.v2100_Months import View_Months
from Views.v2200_Graphs import View_Graphs
from Views.v2300_Transactions import View_Transactions
from Helpers.Messages import Warning_Messages, Error_Messages, Success_Messages
from Views.v9000_Messagees import Error_Message_Dialog, Yes_No_Dialog, Info_Message_Dialog
import Views.vh1001_View_Styles as vh 

#
if TYPE_CHECKING:
    from Controllers.c1001_Main_Frame import Controller_Main_Frame

class View_Main_Frame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialize control object with null. It is assigned by controller 
        self.controlObject : Controller_Main_Frame = None

        self.setFrameShape(QFrame.Box)

        main_frame_layout = QHBoxLayout()

        self.setLayout(main_frame_layout)

        # --- Months
        vertical_frame = QWidget(self)
        vertical_layout = QVBoxLayout(vertical_frame)
        # Import button
        month_import = QPushButton("Import .csv")
        vh.import_button_style(month_import)
        month_import.clicked.connect(self._importCSV)
        vertical_layout.addWidget(month_import)
        # View of months
        self.months_frame = QWidget()
        vh.neutral_widget_style(self.months_frame)
        vh.small_round_widget_corners(self.months_frame)
        #self.months_frame.setStyleSheet("background-color:white; border: 1px solid green;")
        months_layout = View_Months([])
        months_layout.controlObject = self.controlObject # Passing the controller for signals
        self.months_frame.setLayout(months_layout)
        vertical_layout.addWidget(self.months_frame,1)
        main_frame_layout.addWidget(vertical_frame,1)

        # --- Graphs
        graph_widget = QWidget()
        self.graphs_menu = View_Graphs(graph_widget)
#        self.graphs_menu.setStyleSheet("margin: 0px; border: solid brown 2px; background-color: yellow;")
        graph_widget.setStyleSheet("margin: 0px; border: solid brown 2px; background-color: yellow;")
        main_frame_layout.addWidget(graph_widget,4)
        #main_frame_layout.addWidget(self.graphs_menu,4)

        # --- Transactions
        self.scroll_area = QScrollArea()
        vh.scrollable_area_style(self.scroll_area)
        self.scroll_area.setWidgetResizable(True)  # So content can expand inside
        transactions_frame = QWidget()
        transactions = View_Transactions()
        transactions_frame.setLayout(transactions)
        self.scroll_area.setWidget(transactions_frame)

        main_frame_layout.addWidget(self.scroll_area,2)

        vh.small_margin_layout_style(main_frame_layout)

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
            res = self.controlObject.read_months(file_name)
            if isinstance(res, Warning_Messages):
                dialog = Yes_No_Dialog(res.value)
                answer = dialog.exec_()
                if not answer == QDialog.Accepted:
                    return
                else:
                    self.controlObject.read_replace_file(file_name)
                    Info_Message_Dialog("File read successfully.").exec_()
            elif isinstance(res, Error_Messages):
                Error_Message_Dialog(res.value)
                return
            elif isinstance(res, Success_Messages):
                Info_Message_Dialog(res.value)
                return
            
    def update_months_view(self, months:list):
        months_layout = View_Months(months)
        months_layout.controlObject = self.controlObject # Passing the controller for signals
        # Remove old layout (by setting the parent to a temp object)
        QWidget().setLayout(self.months_frame.layout())
        # Assign the new Layout
        self.months_frame.setLayout(months_layout)

    def update_transactions_view(self, transactions:dict):
        transactions_layout = View_Transactions(transactions)
        transactions_frame = QWidget()
        self.scroll_area.setWidget(QWidget())
        self.scroll_area.setWidgetResizable(True)  # So content can expand inside
        transactions_frame.setLayout(transactions_layout)
        self.scroll_area.setWidget(transactions_frame)
