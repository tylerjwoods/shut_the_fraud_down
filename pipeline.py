'''
This file will read from MongoDB Table new_events1
And will then determine if the 
'''

import pandas as pd 
import numpy as np 
#import requests

from predict import predict

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['frauds']
table1 = db['new_events11']
table2 = db['new_events12']

def is_entry_new(object_id):
    '''
    Returns False if the entry is already in the mongodb that talks to website
    '''

    if len(list(table2.find({'object_id': str(object_id)}))) > 0:
        return False
    else:
        return True

def risk_factor(df):
    '''
    create a new variable called risk_factor that is
        'low' if the prediction is less than 0.25,
        'medium' if the prediction is greater than 0.5,
         and 'high' if the prediction is greater than 0.5.
    '''
    if df['fraud_probability'] == 1:
        df['risk_factor'] = 'Unable to Predict'
    elif df['fraud_probability'] < 0.25:
        df['risk_factor'] = 'low'
    elif df['fraud_probability'] < 0.5:
        df['risk_factor'] = 'medium'
    else:
        df['risk_factor'] = 'high'
    return df

def pipeline():
    # get data from table 1
    new_data = table1.find()

    # import data into a pandas dataframe
    df_new = pd.DataFrame(list(new_data))

    # Loop through each line of the dataframe
    for i, each_object in enumerate(df_new['object_id']):
        # determine if each entry in df_new is already in table2
        if is_entry_new(each_object):
            # get the prediction from predict.py
            df_1 = df_new.iloc[i,:].copy()
            df_1 = predict(df_1)


            # create a new variable called risk_factor that is
            # 'low' if the prediction is less than 0.25,
            # 'medium' if the prediction is greater than 0.5,
            # and 'high' if the prediction is greater than 0.5.
            df_1 = risk_factor(df_1)

            # create a dictionary that will be used to store items in mongodb
            d = {
                'sequence': str(df_1['sequence_number']),
                'object_id': str(df_1['object_id']),
                'name': df_1['name'],
                'org_name': df_1['org_name'],
                'fraud_probability': df_1['fraud_probability'],
                'risk_factor': df_1['risk_factor']
            }

            # remove the entry from table 1
            table1.delete_one({'object_id':str(df_1['object_id'])})
            # store d into mongodb
            table2.insert_one(d)



if __name__ == '__main__':
    pipeline()