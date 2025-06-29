
from Views.v2001_Months import View_Months

class Controller_Months():
    def __init__(self, parent=None):
        self.viewObject = View_Months()
        self.update_view()

    def update_view(self):
        # Get months from model...
        temp_list = ["January 2025", "February 2025", "March 2025", "April 2025"]
        self.viewObject.update(temp_list)