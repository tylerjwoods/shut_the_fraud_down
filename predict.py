'''
This script will read in NEW pandas datframe info,
Make a prediction on it (probability that it is fraud),
and then return a dataframe with that prediction on it.
'''

import pandas as pd 
import numpy as np 
import pickle 

from src.clean_new_data import clean_new_data

# from pymongo import MongoClient
# client = MongoClient('localhost', 27017)
# db = client['fraud']
# table = db['events']


# def load_clean_into_pandas(request_info):
#     '''
#     inputs
#     ------
#     request_info: json formatted info that will be formatted into 
#     '''
#     df = clean_new_data(df)

#     return df


def predict(request_info):
    '''
    inputs
    ------
    request_info: pandas dataframe 
    '''

    # load request_info into a pandas dataframe and clean it using clean_new_data
    # df = pd.read_json(request_info)
    df_cleaned = clean_new_data(request_info)

    # set x_test to the cleaned dataframe
    X_test = np.array(df_cleaned)

    # load saved pickled model
    with open('models/grad_boost_model.p', 'rb') as mod:
        model = pickle.load(mod)

    # calcluate the fraud probability of the input data using the model's predict_proba method
    # try the predict_proba. if it cannot be calculated, set it equal to 0.
    try:
        probs = model.predict_proba(X_test.reshape(1,-1))[:, 1]
    except:
        probs = [1,1]

    # add the probs to the original dataframe
    request_info['fraud_probability'] = np.around(probs[0], 3)
    #print(request_info['fraud_probability'])

    # return the dataframe with the predictions
    return request_info
    