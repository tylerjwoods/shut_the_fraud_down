from flask import Flask, render_template, request, jsonify 
import pickle
import numpy as np

from predict import predict
from test_script import test_script

from pymongo import MongoClient


# Create app
app = Flask(__name__)

# Render home page
@app.route('/',methods=['GET'])
def home():
    return render_template('new_home.html')

# Execute logic of prediction
@app.route('/table', methods=['GET'])
def table():


    # connect to database
    client = MongoClient('localhost', 27017)
    db = client['frauds']
    table = db['new_events12']

    events = table.find().sort([('sequence', -1)]).sort([('fraud_probability', -1)]).limit(50)

    # render the template and pass the events
    return render_template('home.html', data=events)



if __name__ == '__main__':
    # load saved pickled model
    with open('models/grad_boost_model.p', 'rb') as mod:
        model = pickle.load(mod)

    # connect to database
    client = MongoClient('localhost', 27017)
    db = client['frauds']
    table = db['new_events12']
    
    # run flask app
    app.run(host='0.0.0.0', port=8000, debug=True)