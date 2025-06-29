
from Views.v2001_View_Months import View_Months
from Model.m2000_Model_Months import Model_Months

class Controller_Months():
    def __init__(self, parent=None):
        self.viewObject = View_Months()
        self.modelObject = Model_Months()