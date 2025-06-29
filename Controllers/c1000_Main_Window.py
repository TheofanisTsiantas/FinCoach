# Imports of libraries
import sys
from PyQt5.QtWidgets import QApplication

# Imports of custom modules
from Views.v1000_Main_Window import View_Main_Window

class Controller_Main_Window:
    def __init__(self):
        # Create view of the main window
        app = QApplication(sys.argv) # QApplication must get initialized prior to any QObject use
        app.setApplicationName("My App")      

        self.viewObject = View_Main_Window()
        self.viewObject.show()
        #
        #self.modelObject = Model_Months()
        sys.exit(app.exec_())
