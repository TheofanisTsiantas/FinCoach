import pandas as pd

from Helpers.Messages import Error_Messages, Warning_Messages, Success_Messages

class Model:
    def __init__(self):
        self.data = pd.DataFrame()

    def read_file(self, path:str):
        if not path.lower().endswith(".csv"):
            return []
        try:
            # Read file
            df = self._read_file(path)
            # Transform date to appropriate format
            month_year = df['Date'].unique()
            # Check for error in file
            if len(month_year)>1:
                return Error_Messages.INVALID_FORMAT
            elif not month_year:
                return Error_Messages.EMPTY_DATA
        # Check for value read exceptions
        except Exception as e:
            Error_Messages.EXCEPTION += e
            return Error_Messages.EXCEPTION
        # Warn in case of existing file
        if month_year in self.get_months():
            return Warning_Messages.FILE_EXISTS
        # Read file and append existing model
        df = self._read_file(path)
        self.data = pd.concat([self.data, df], ignore_index=True)
        return Success_Messages.FILE_READ

    def read_replace_file(self, path:str):
        # Get a dataframe with the read data
        df = self._read_file(path)
        # Locate the month to be deleted from the model
        replace_month = df['Date'][0]
        # Delete month from model
        self.data = self.data[self.data['Date']!=replace_month]
        # Concatinate
        self.data = pd.concat([self.data, df], ignore_index=True)
        
    def get_months(self):
        return self.data['Date'].unique()

    def _read_file(self, path:str):
        # Read the month with the replacement data
        df = pd.read_csv(path, sep=";")
        # Remove unecessary data
        df.drop(columns=['ZKB reference', 'Reference number', 'Credit CHF', 'Balance CHF'], inplace=True)
        # Transform date to appropriate format
        df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors="coerce")
        df['Date'] = df['Date'].dt.month.astype(str) + "-" + df['Date'].dt.year.astype(str)
        return df