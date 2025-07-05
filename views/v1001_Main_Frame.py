# The frame displaying the finance data evolution

from PyQt5.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QLabel,
    QPushButton,
    QFileDialog,
    QDialog, QMessageBox
)

from PyQt5.QtCore import pyqtSlot
from typing import TYPE_CHECKING

#
from Views.v2001_Months import View_Months
from Views.v2002_Graphs import View_Graphs
from Views.v2002_Transactions import View_Transactions
from Helpers.Messages import Warning_Messages, Error_Messages, Success_Messages
from Views.v9000_Messagees import Error_Message_Dialog, Yes_No_Dialog, Info_Message_Dialog
#
if TYPE_CHECKING:
    from Controllers.c1001_Main_Frame import Controller_Main_Frame

IMPORT_BUTTON_STYLE = """ QPushButton { background-color: #e8d8ac; border-radius: 8px;padding:5px; border: 1px solid grey; }"""

class View_Main_Frame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialize control object with null. It is assigned by controller 
        self.controlObject : Controller_Main_Frame = None

        self.setFrameShape(QFrame.Box)
        self.setStyleSheet("border: 1px solid black; background-color: #eeeeee;")

        main_frame_layout = QHBoxLayout()
        main_frame_layout.setContentsMargins(5, 5, 5, 5)
        self.setLayout(main_frame_layout)

        # --- Months
        vertical_frame = QWidget(self)
        vertical_frame.setStyleSheet("border: 0.5px solid black;")
        vertical_layout = QVBoxLayout(vertical_frame)
        # Import button
        month_import = QPushButton("Import .csv")
        month_import.setStyleSheet(IMPORT_BUTTON_STYLE)
        month_import.clicked.connect(self._importCSV)
        vertical_layout.addWidget(month_import)
        # View of months
        self.months_frame = QWidget()
        self.months_frame.setStyleSheet("background-color:white; border: 1px solid green;")
        months_layout = View_Months([])
        self.months_frame.setLayout(months_layout)
        vertical_layout.addWidget(self.months_frame,1)
        main_frame_layout.addWidget(vertical_frame,1)

        # --- Graphs
        self.graphs_menu = View_Graphs(self)
        main_frame_layout.addWidget(self.graphs_menu,4)

        # --- Info
        info_menu = QWidget()
        info_menu.setStyleSheet("border: 1px solid black;")
        transactions = View_Transactions()
        info_menu.setLayout(transactions)

        # main_frame_layout.addWidget(info_menu)
        main_frame_layout.addWidget(info_menu,2)

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
        # Remove old layout (by setting the parent to a temp object)
        QWidget().setLayout(self.months_frame.layout())
        # Assign the new Layout
        self.months_frame.setLayout(months_layout)