# Imports of libraries

# Imports of custom modules
from Views.v1000_Main_Window import View_Main_Window

class Controller_Main_Window:
    def __init__(self):
        # Create view of the main window 
        self.viewObject = View_Main_Window()
        self.viewObject.show()
        #
        #self.modelObject = Model_Months()
