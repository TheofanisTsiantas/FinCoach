# Imports of libraries

# Imports of custom modules
from Views.v1001_Main_Frame import View_Main_Frame
from Model.m0000_Model import Model

class Controller_Main_Frame:
    def __init__(self, View_Main_Frame:View_Main_Frame, model:Model):
        self.view_object = View_Main_Frame
        self.model = model

    def read_months(self, path : str):
        return self.model.read_file(path)
    
    def read_replace_file(self, path : str):
        return self.model.read_replace_file(path)