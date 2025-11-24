import pandas as pd

from Helpers import Categories


def import_data(path:str):
    # Read the month with the replacement data
    df = pd.read_csv(path, sep=";")
    # Remove unecessary data
    df = df[['Date', 'Booking text', 'Debit CHF', 'Value date']]
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

def get_expenses(data:pd):
    # This method returns a dictionary with key=category (super market, etc.) and value a list of lists l = [l1 l2]
    # l1: list of months, l2: sum of expenses for each month. Precondition: len(l1)==len(l2)
    return_dictionary = {}
    for category in Categories.TRANSACTION_CATEGORIES.keys():
        df = data[data[category] != ""][['Date','Debit CHF']] # Get dataframe for each category, excluding zero values
        df['Date'] = pd.to_datetime(df['Date'], format='%m-%Y', errors='coerce') # Convert date to datetime object (for sorting later))
        df['Date'] = df['Date'].dt.strftime('%m-%Y') # Keep only month-year
        cat_expenses_by_month = df.groupby('Date', as_index=False) # Group categories by identical dates (MM-YYYY)
        cat_expenses_by_month = cat_expenses_by_month.sum() # Some all expenses for each date
        cat_expenses_by_month = cat_expenses_by_month.sort_values(by='Date') # Sort by date
        cat_expenses_by_month_list = [cat_expenses_by_month['Date'].tolist(), cat_expenses_by_month['Debit CHF'].tolist()]
        return_dictionary[category] = cat_expenses_by_month_list

    return return_dictionary