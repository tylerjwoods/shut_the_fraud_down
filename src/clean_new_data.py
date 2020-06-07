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

def clean_new_data(df):
    '''
    Cleans the input dataframe. Dataframe is a SINGLE entry (i.e., a series)
    '''
    ### DELETE THIS SINCE NEW DATA WON'T HAVE FRAUD OR NOT ###
    # Create a new column called 'fraud' that contains if the account is fradulent
    #frauds = set(['fraudster_event', 'fraudster', 'fraudster_att'])
    #df['fraud'] = df['acct_type'].apply(lambda x: True if x in frauds else False)
    

    # Fill NA values of column 'delivery_method' with 4
    delivery_methods = [0., 1., 3.]
    if df['delivery_method'] not in delivery_methods:
        df['delivery_method']=4


    # Create a new column called 'previous_payouts_length_' which will be 0
    # if the length is zero, otherwise it is 1.
    df['previous_payouts_length'] = len(df['previous_payouts'])
    df['previous_payouts_length_'] = int(df['previous_payouts_length'] > 1)

    # fb_published was found to have a high indication during eda, don't need to filter it

    # Create a new column called 'ticket_type_length' which will be True if the length of ticket_type is 0
    df['ticket_type_length'] = len(df['ticket_types']) < 1

    ### Gross Profits ###
    # Create a new column called 'gross_profits' that multiples the cost of each ticket
    # in ticket_types by the quanitity sold. This will then be used as a dummie variable.
    #gross_profits_list = []
    gross_profits = 0
    for j in df['ticket_types']:
        gross_profits += j['cost'] * j['quantity_total']
    df['gross_profits'] = gross_profits

    # Create a new column called gross_profits_dummies that will use gross_profit_dummie function
    df['gross_profits_dummie'] = gross_profit_dummie(df['gross_profits'])

    # channels was found to have a high indiction during eda, don't need to filter it

    # user_type was found to have a high indication during eda, don't need to filter it

    # sale_duration2 was found to have a high indction during ead, don't need to filter it

    # Grab only the columns that our group found to be important
    df_cleaned = df[['delivery_method', 'fb_published', 'ticket_type_length', \
        'gross_profits_dummie','channels', 'user_type', 'sale_duration']].copy()

    #df_cleaned.to_csv('data/cleaned_df.csv', index=False)

    return df_cleaned