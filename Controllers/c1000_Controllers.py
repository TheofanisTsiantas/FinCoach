# Imports of libraries
import sys
from PyQt5.QtWidgets import QApplication

# Imports of custom modules
from Controllers.c2001_Months import Controller_Months
from Controllers.c1000_Main_Window import Controller_Main_Window
from Model.m0000_Model import Model

class Controllers:
    def __init__(self, model:Model):
        # Initiate the Qt application
        app = QApplication(sys.argv) # QApplication must get initialized prior to any QObject use
        app.setApplicationName("My App")     
        
        #
        self.main_window_controller = Controller_Main_Window(model)
        self.month_controller = Controller_Months()
        
        # Ensure correct termination of the Qt application
        sys.exit(app.exec_())