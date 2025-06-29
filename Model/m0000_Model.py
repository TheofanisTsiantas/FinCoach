import pandas as pd

from Helpers.Messages import Error_Messages, Warning_Messages

class Model:
    def __init__(self):
        self.data = pd.DataFrame()
        # temp
        self.data = pd.read_csv('/Users/theofanistsiantas/Downloads/test.csv', sep=";")
        print(f"{self.data.head()}")
        self.data["Date"] = pd.to_datetime(self.data["Date"], dayfirst=True, errors="coerce")
        self.month_year = (self.data['Date'].dt.month.astype(str) + "-" + self.data['Date'].dt.year.astype(str)).unique() # Convert to date time object

    def read_file(self, path:str):
        if not path.lower().endswith(".csv"):
            return []
        try:
            # Read file
            df = pd.read_csv(path, sep=";")
            # Transform date to appropriate format
            df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")
            month_year = (df['Date'].dt.month.astype(str) + "-" + df['Date'].dt.year.astype(str)).unique()
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
        if month_year in self.month_year:
            return Warning_Messages.FILE_EXISTS
        
        return self.month_year

    def get_months(self, path:str):
        return self.month_year

