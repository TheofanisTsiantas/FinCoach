import pandas as pd

from Helpers import Categories


def import_data(path:str):
    # Read the month with the replacement data
    df = pd.read_csv(path, sep=";")
    # Remove unecessary data
    df.drop(columns=['ZKB reference', 'Reference number', 'Credit CHF', 'Balance CHF'], inplace=True)
    # Remove invalid data
    df.dropna(inplace=True)
    # Transform date to appropriate format
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors="coerce")
    df['Date'] = df['Date'].dt.month.astype(str) + "-" + df['Date'].dt.year.astype(str)
    # Assign categories to dataframe (as empty columns)
    for category in Categories.TRANSACTION_CATEGORIES.keys():
        df[category] = ""
    # Move data to the categories
    for idx, row in df.iterrows():
        category_assigned = False
        for category, keywords in Categories.TRANSACTION_CATEGORIES.items():
            for keyword in keywords:
                if keyword.lower() in row['Booking text'].strip().lower():
                    df.at[idx, category]=row['Booking text']
                    category_assigned = True
                    break
            if category_assigned == True:
                break
        if category_assigned==False:
            df.at[idx, 'Other']=row['Booking text']
    # Delete the booking text category
    df.drop(columns=['Booking text'], inplace=True)
    return df
