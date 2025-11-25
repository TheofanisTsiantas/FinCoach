# Imports of libraries

# Imports of custom modules
from Views.v1100_Main_Frame import View_Main_Frame
from Model.m0000_Model import Model

from Helpers.Messages import Success_Messages


class Controller_Main_Frame:
    def __init__(self, View_Main_Frame:View_Main_Frame, model:Model):
        self.view_object = View_Main_Frame
        self.model = model
        self.selected_month = "" # The controller knows the currently selected month (if any)

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
    
    # Commands model to override its data
    def overwrite_dataframe(self, path : str):
        self.model.overwrite_dataframe(path)
        # Reset selected month to none
        self.selected_month = ""
        # Update the view of the months
        self._update_months_view()
        # Update the expense evolution plot
        self._update_expense_evolution_graph_view()
        # Set transactions to empty list
        self._update_transactions_view()
        # Set pie chart to empty
        self._update_expense_distribution_graph_view()
        return Success_Messages.DATA_READ

    # Get data as a dictionary
    def get_Data_Dict(self):
        return self.model.get_Data_Dict()

    # Controller fetches appropriate data of newly selected month to update correspoding view graphs 
    def new_month_selected(self, selected_month=""):
        self.selected_month = selected_month;
        # Inform the cotroller that transactions must be updated according to selected month
        self._update_transactions_view()
        # Inform the cotroller that pie view must be updated according to selected month
        self._update_expense_distribution_graph_view()

    # private method which calls the view to update months
    def _update_months_view(self):
        # Get current months from model
        months = self.model.get_months()
        months.sort()
        # Call view update
        self.view_object.update_months_view(months)
        # Remove any list with transactions
        self._update_transactions_view()

    # Update the view of the transactions for a selected month
    def _update_transactions_view(self):
        if self.selected_month=='':
            self.view_object.update_transactions_view({})
        else:
            transactions = self.model.get_transactions(self.selected_month)
            self.view_object.update_transactions_view(transactions)

    # Update the pie chart of the expense distribution per month
    def _update_expense_distribution_graph_view(self):
        if self.selected_month=='':
            self.view_object.update_expense_distribution_graph_view({}, "")
        else:
            expense_distribution, total_monthly_cost = self.model.get_expense_distribution(self.selected_month)
            plot_title = self.selected_month+"(total: "+str(total_monthly_cost)+" CFH)";
            self.view_object.update_expense_distribution_graph_view(expense_distribution, plot_title)

    # Update the scatter chart of the transaction distribution through time
    def _update_expense_evolution_graph_view(self):
        expense_evolution = self.model.get_expense_evolution()
        self.view_object.update_expense_evolution_graph_view(expense_evolution)
