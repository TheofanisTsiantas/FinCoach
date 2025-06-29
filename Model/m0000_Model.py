import pandas as pd

class Model:
    def __init__(self):
        self.data = pd.DataFrame()
        # temp
        self.data = pd.read_csv('/Users/theofanistsiantas/Downloads/test.csv', sep=";")
        print(f"{self.data.head()}")
        self.data["Date"] = pd.to_datetime(self.data["Date"], dayfirst=True, errors="coerce")
        self.month_year = (self.data['Date'].dt.month.astype(str) + "-" + self.data['Date'].dt.year.astype(str)).unique() # Convert to date time object

    def get_months(self):
        return self.month_year

