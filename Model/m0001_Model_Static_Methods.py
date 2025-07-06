import pandas as pd

def import_data(path:str):
    # Read the month with the replacement data
    df = pd.read_csv(path, sep=";")
    # Remove unecessary data
    df.drop(columns=['ZKB reference', 'Reference number', 'Credit CHF', 'Balance CHF'], inplace=True)
    # Transform date to appropriate format
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors="coerce")
    df['Date'] = df['Date'].dt.month.astype(str) + "-" + df['Date'].dt.year.astype(str)
    return df
