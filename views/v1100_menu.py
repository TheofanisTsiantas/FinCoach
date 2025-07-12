# The menu of the application

# Imports of libraries
from PyQt5.QtWidgets import QAction,QMenuBar
from PyQt5.QtCore import pyqtSlot

class Menu(QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)

        file_menu = self.addMenu("&File")
        
        new_action = QAction("&New", self)
        new_action.triggered.connect(self.show_message)
        file_menu.addAction(new_action)

        exit_action = QAction("&Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        edit_menu = self.addMenu("&Edit")
        cut_action = QAction("Cu&t", self)
        edit_menu.addAction(cut_action)

    @pyqtSlot()
    def show_message(self):
        from PyQt5.QtWidgets import QMessageBox
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("This is a message box")
        msg.setWindowTitle("Information")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

