# Imports of libraries

# Imports of custom modules
from Views.v1001_Main_Frame import View_Main_Frame
from Model.m0000_Model import Model

from Helpers.Messages import Success_Messages


class Controller_Main_Frame:
    def __init__(self, View_Main_Frame:View_Main_Frame, model:Model):
        self.view_object = View_Main_Frame
        self.model = model

    def read_months(self, path : str):
        res = self.model.read_file(path)
        # In case of successful read update the view
        if isinstance(res, Success_Messages):
            self._update_months_view()
        return res
    
    def read_replace_file(self, path : str):
        # In case of successful read update the view
        res = self.model.read_replace_file(path)
        if isinstance(res, Success_Messages):
            self._update_months_view()
        return res
    
    def _update_months_view(self):
        # Get current months from model
        months = self.model.get_months()
        months.sort()
        # Call view update
        self.view_object.update_months_view(months)
        # Remove any list with transactions
        self.update_transactions_view()

    def update_transactions_view(self, selected_month:str=''):
        if selected_month=='':
            self.view_object.update_transactions_view({})
        else:
            transactions = self.model.get_transactions(selected_month)
            self.view_object.update_transactions_view(transactions)