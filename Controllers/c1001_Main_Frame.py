# Imports of libraries

# Imports of custom modules
from Views.v1100_Main_Frame import View_Main_Frame
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
            # Update the view of the months
            self._update_months_view()
            # Update the expenses plot
            self._update_expense_evolution_graph_view()            
        return res
    
    def read_replace_file(self, path : str):
        # In case of successful read update the view
        res = self.model.read_replace_file(path)
        if isinstance(res, Success_Messages):
            # Update the view of the months
            self._update_months_view()
            # Update the expenses plot
            self._update_expense_evolution_graph_view()
        return res
    
    def _update_months_view(self):
        # Get current months from model
        months = self.model.get_months()
        months.sort()
        # Call view update
        self.view_object.update_months_view(months)
        # Remove any list with transactions
        self.update_transactions_view()

    # Update the view of the transactions for a selected month
    def update_transactions_view(self, selected_month:str=''):
        if selected_month=='':
            self.view_object.update_transactions_view({})
        else:
            transactions = self.model.get_transactions(selected_month)
            self.view_object.update_transactions_view(transactions)

    # Update the pie chart of the expense distribution per month
    def update_expense_distribution_graph_view(self, selected_month:str=''):
        if selected_month=='':
            self.view_object.update_expense_distribution_graph_view({})
        else:
            expense_distribution, total_monthly_cost = self.model.get_expense_distribution(selected_month)
            plot_title = selected_month+"(total: "+str(total_monthly_cost)+" CFH)";
            self.view_object.update_expense_distribution_graph_view(expense_distribution, plot_title)

    # Update the scatter chart of the transaction distribution through time
    def _update_expense_evolution_graph_view(self):
        expense_evolution = self.model.get_expense_evolution()
        self.view_object.update_expense_evolution_graph_view(expense_evolution)
