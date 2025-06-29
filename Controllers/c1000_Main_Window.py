# Imports of libraries

# Imports of custom modules
from Views.v1000_Main_Window import View_Main_Window
from Controllers.c1001_Main_Frame import Controller_Main_Frame
from Model.m0000_Model import Model

class Controller_Main_Window:
    def __init__(self, model:Model):

        # Create view of the main window (it also creates the main frame)
        self.view_object = View_Main_Window()
        self.view_object.show()
        
        # ------------------- Controllers
        # 1. Controller of the main frame
        self.main_frame_controller = Controller_Main_Frame(self.view_object.main_frame, model)   # Binding view to controller 
        self.main_frame_controller.view_object.controlObject = self.main_frame_controller # Binding controller to view
        #
        #self.modelObject = Model_Months()
