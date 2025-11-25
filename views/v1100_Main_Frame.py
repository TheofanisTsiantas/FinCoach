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

import csv 
import json
from pathlib import Path

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

        vertical_frame = QWidget(self)
        vertical_layout = QVBoxLayout(vertical_frame)

        # --- Data import/save
        data_import = QPushButton("Import data")
        vh.import_button_style(data_import)
        data_import.clicked.connect(self._importData)
        vertical_layout.addWidget(data_import)
        data_save = QPushButton("Save data")
        vh.save_button_style(data_save)
        vertical_layout.addWidget(data_save)
        data_save.clicked.connect(self._saveData)

        # --- Months
        # Import button
        month_import = QPushButton("Import month")
        vh.import_button_style(month_import)
        month_import.clicked.connect(self._importMonth)
        vertical_layout.addWidget(month_import)
        # View of months
        self.months_frame = QWidget()
        vh.neutral_widget_style(self.months_frame)
        vh.small_round_widget_corners(self.months_frame)
        #self.months_frame.setStyleSheet("background-color:white; border: 1px solid green;")
        months_layout = View_Months([])
        self.months_frame.setLayout(months_layout)
        vertical_layout.addWidget(self.months_frame,1)
        main_frame_layout.addWidget(vertical_frame,1)

        # --- Graphs
        self.graphs_widget = QWidget()
        self.graphs_menu = View_Graphs(self.graphs_widget)
        self.graphs_widget.setStyleSheet("margin: 0px; border: solid brown 2px; background-color: yellow;")
        main_frame_layout.addWidget(self.graphs_widget,4)

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
    def _importMonth(self):
        # Open the file dialog
        file_names,_ = QFileDialog.getOpenFileNames(
        self,                          # parent
        "Select CSV file",             # dialog title
        "",                            # initial directory
        "CSV Files (*.csv)",           # ;All Files (*);" --> Filters
        "CSV Files (*.csv)"            # Present active filter
        )
        if (self.controlObject == None):
            return
        for file_name in file_names:
            res = self.controlObject.read_months(file_name)
            if isinstance(res, Warning_Messages):
                dialog = Yes_No_Dialog(file_name+": "+res.value)
                answer = dialog.exec_()
                if not answer == QDialog.Accepted:
                    continue
                else:
                    self.controlObject.read_replace_file(file_name)
                    Info_Message_Dialog("File read successfully.").exec_()
            elif isinstance(res, Error_Messages):
                Error_Message_Dialog(res.value).exec_()
                return
            elif isinstance(res, Success_Messages):
                Info_Message_Dialog(res.value).exec_()

    @pyqtSlot()
    def _importData(self):
        # Open the file dialog
        file_name = QFileDialog.getOpenFileName(
        self,                      # parent
        "Select JSON file",        # dialog title
        "",                        # initial directory
        "JSON Files (*.json)",     # Available filters
        "JSON Files (*.json)"      # Present active filter
        )
        if file_name[0]=='':
            return
        if (self.controlObject == None):
            return
        res = self.controlObject.get_Data_Dict()
        if res:
            dialog = Yes_No_Dialog(Warning_Messages.DATA_EXISTS.value)
            answer = dialog.exec_()
            if not answer == QDialog.Accepted:
                return
        res = self.controlObject.overwrite_dataframe(file_name[0])
        if isinstance(res, Error_Messages):
            Error_Message_Dialog(res.value).exec_()
            return
        elif isinstance(res, Success_Messages):
            Info_Message_Dialog(res.value).exec_()
    
    @pyqtSlot()
    def _saveData(self):
        # Open the file dialog
        file_name = QFileDialog.getSaveFileName(
        self,                        # parent
        "Save data as json",         # dialog title
        "",                          # initial directory
        "JSON Files (*.json);",      # Available filters
        "JSON Files (*.json)"        # Present active filter 
        )
        if file_name[0]=='':
            return
        if (self.controlObject == None):
            return
        res = self.controlObject.get_Data_Dict()
        if not res:
            Error_Message_Dialog(Error_Messages.EMPTY_SAVE_DATA.value).exec_()
            return
        _filename = file_name[0]+".json"

        if Path(_filename).exists():
            dialog = Yes_No_Dialog(Warning_Messages.FILE_SAVE_EXISTS.value)
            answer = dialog.exec_()
            if not answer == QDialog.Accepted:
                return
            else:
                Path(_filename).unlink() # Deletes file
        with open(_filename, "w") as f:
            json.dump(res, f)
        Info_Message_Dialog(Success_Messages.FILE_SAVE.value).exec()

    # Update the view of the list of months which have been read
    def update_months_view(self, months:list):
        months_layout = View_Months(months, self.select_month)
        # Remove old layout (by setting the parent to a temp object)
        QWidget().setLayout(self.months_frame.layout())
        # Assign the new Layout
        self.months_frame.setLayout(months_layout)

    # Update the view of the transactions for a selected month
    # transactions:dict --> { CATEGORY : [  [cost, description]  ,  [cost, description]  ] }
    def update_transactions_view(self, transactions:dict):
        transactions_layout = View_Transactions(transactions, self.transaction_deleted)
        transactions_frame = QWidget()
        self.scroll_area.setWidget(QWidget())
        self.scroll_area.setWidgetResizable(True)  # So content can expand inside
        transactions_frame.setLayout(transactions_layout)
        self.scroll_area.setWidget(transactions_frame)

    # Update the pie chart of the expense distribution per month
    # expense_distribution:dict --> { CATEGORY : XX% of monthly cost }
    def update_expense_distribution_graph_view(self, expense_distribution:dict, plot_title:str):
        self.graphs_menu.update_expense_distribution_graph(expense_distribution, plot_title)

    # Update the scatter chart of the transaction distribution through time
    def update_expense_evolution_graph_view(self, expense_evolution:dict):
        self.graphs_menu.update_expense_evolution_graph(expense_evolution)

    # Called by the view when a delete-transaction signal has been emmited. Notifies the controller. 
    def transaction_deleted(self, transaction_id:int=-1, transaction_name:str="", transaction_value:float=0.0, transaction_category:str=""):
        # Check input 
        if transaction_id==-1 or transaction_name=="" or transaction_category=="":
            return Error_Messages.TRANS_DEL_FAILED
        self.controlObject.delete_transaction(transaction_id, transaction_name, transaction_value, transaction_category)
        
    # Called by the view when a select-month signal has been emmited. Notifies the controller.
    def select_month(self, month:str):
        self.controlObject.new_month_selected(month);