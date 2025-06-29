# Imports of libraries
import sys
from PyQt5.QtWidgets import QApplication

# Imports of custom modules
from Controllers.c2000_Controller_Months import Controller_Months
from views.v1000_Start_Window import Start_Window

class Controllers:
    def __init__(self):
        #
        app = QApplication(sys.argv)
        app.setApplicationName("My App")
        window = Start_Window()
        window.show()
        sys.exit(app.exec_())

        self.month_controller = Controller_Months()