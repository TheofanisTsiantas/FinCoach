import pandas as pd
import math
import io

from Helpers.Messages import Error_Messages, Warning_Messages, Success_Messages
from Helpers import Categories

import Model.m0001_Model_Static_Methods as msm

class Model:
    def __init__(self):
        self.data = pd.DataFrame()

    def read_file(self, path:str):
        if not path.lower().endswith(".csv"):
            return []
        try:
            # Read file
            df = msm.import_data(path)
            # Transform date to appropriate format
            month_year = df['Date'].unique()
            # Check for error in file
            if len(month_year)>1:
                return Error_Messages.INVALID_FORMAT
            elif not month_year:
                return Error_Messages.EMPTY_IMPORT_DATA
        # Check for value read exceptions
        except Exception as e:
            Error_Messages.EXCEPTION += e
            return Error_Messages.EXCEPTION
        # Warn in case of existing file
        if month_year[0] in self.get_months():
            return Warning_Messages.FILE_IMPORT_EXISTS
        # Read file and append existing model
        df = msm.import_data(path)
        self.data = pd.concat([self.data, df], ignore_index=True)
        return Success_Messages.FILE_READ

    def read_replace_file(self, path:str):
        # Get a dataframe with the read data
        df = msm.import_data(path)
        # Locate the month to be deleted from the model
        replace_month = df['Date'][0]
        # Delete month from model
        self.data = self.data[self.data['Date']!=replace_month]
        # Concatinate
        self.data = pd.concat([self.data, df], ignore_index=True)
        return Success_Messages.FILE_READ
        
    def get_months(self):
        if self.data.empty:
            return []
        elif 'Date' not in self.data.columns: 
            return []
        self.data.to_csv('myData.csv', index=False);
        return self.data['Date'].unique()  
    
    # Returns a dictionary of the transactions for a selected month
    # Dict (each value is a list of lists): { CATEGORY : [  [cost, description]  ,  [cost, description]  ] }
    def get_transactions(self, month:str):
        if self.data.empty:
            return {}
        elif 'Date' not in self.data.columns: 
            return {}
        # Initialize return directory
        transactions = {}
        for category in Categories.TRANSACTION_CATEGORIES:
            if category not in self.data.columns:
                continue
            df = self.data[self.data['Date']==month][['Debit CHF', category]] # Extract df view
            df = df[~(df[category]=="")] # Remove empty cells
            transactions[category] = df.values.tolist()
        return transactions
    
    # Returns the cost distribution (percentage) of each category in the total expenses of the month
    def get_expense_distribution(self, selected_month):
        cost_distribution = {}
        month_transactions = self.get_transactions(selected_month)
        total_monthly_cost = 0
        for cat, transactions in month_transactions.items():
            total_category_costs = 0
            for category_cost in transactions:
                total_category_costs += category_cost[0]
            total_monthly_cost += total_category_costs
            cost_distribution[cat] = total_category_costs
        for cat in month_transactions.keys():
            cost_distribution[cat] = round(cost_distribution[cat]/total_monthly_cost*100,1)
        if sum(cost_distribution.values())-100>0.5 or sum(cost_distribution.values())<99.5:
            return {},0
        return cost_distribution, math.ceil(total_monthly_cost)
    
    def get_expense_evolution(self):        
        if self.data.empty:
            return {}
        return msm.get_expenses(self.data)

    def get_Data_Dict(self):
        return self.data.to_dict();