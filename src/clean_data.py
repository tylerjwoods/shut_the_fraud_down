import numpy as np 
import pandas as pd 

def gross_profit_dummie(x):
    '''
    Seperates the gross values by their percentiles. 
    0 being no gross profits made,
    1 being less than $75 made
    2 being less than $345 made
    3 being less than $1356 made
    4 being more than $1356 made
    '''
    if x < 1:
        return 0
    elif x < 75:
        return 1
    elif x < 345:
        return 2
    elif x < 1356:
        return 3
    else:
        return 4

def clean_data(df):
    '''
    Cleans the input dataframe.
    '''
    # Create a new column called 'fraud' that contains if the account is fradulent
    frauds = set(['fraudster_event', 'fraudster', 'fraudster_att'])
    df['fraud'] = df['acct_type'].apply(lambda x: True if x in frauds else False)
    

    # Fill NA values of column 'delivery_method' with 4
    df['delivery_method'].fillna(4, inplace=True)


    # Create a new column called 'previous_payouts_length_ which will be 0
    # if the length is zero, otherwise it is 1.
    df['previous_payouts_length'] = df['previous_payouts'].apply(lambda x: len(x))
    df['previous_payouts_length_'] = df['previous_payouts_length'].apply(lambda x: 1 if x>1 else 0)

    # fb_published was found to have a high indication during eda, don't need to filter it

    # Create a new column called 'ticket_type_length' which will be True if the length of ticket_type is 0
    df['ticket_type_length'] = (df['ticket_types'].apply(lambda x: len(x)) < 1)

    ### Gross Profits ###
    # Create a new column called 'gross_profits' that multiples the cost of each ticket
    # in ticket_types by the quanitity sold. This will then be used as a dummie variable.
    gross_profits_list = []
    for row in df['ticket_types']:
        gross_profits = 0
        for i in range(len(row)):
            gross_profits += row[i]['cost'] * row[i]['quantity_sold']
        gross_profits_list.append(gross_profits)
    df['gross_profits'] = gross_profits_list

    # Create a new column called gross_profits_dummies that will use gross_profit_dummie function
    df['gross_profits_dummie'] = df['gross_profits'].apply(lambda x: gross_profit_dummie(x))

    # channels was found to have a high indiction during eda, don't need to filter it

    # user_type was found to have a high indication during eda, don't need to filter it

    # sale_duration2 was found to have a high indction during ead, don't need to filter it

    # Grab only the columns that our group found to be important
    df_cleaned = df[['fraud', 'delivery_method','fb_published', 'ticket_type_length', \
        'gross_profits_dummie','channels', 'user_type', 'sale_duration2']].copy()

    df_cleaned.to_csv('data/cleaned_df.csv', index=False)

    return df_cleaned