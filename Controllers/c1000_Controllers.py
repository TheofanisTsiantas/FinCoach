# Imports of libraries
import sys
from PyQt5.QtWidgets import QApplication

# Imports of custom modules
from Controllers.c2001_Months import Controller_Months
from Controllers.c1000_Main_Window import Controller_Main_Window

class Controllers:
    def __init__(self):
        self.main_window_controller = Controller_Main_Window()
        self.month_controller = Controller_Months()