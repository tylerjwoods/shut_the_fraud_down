from flask import Flask, render_template, request, jsonify 
import pickle
import numpy as np
from jinja2 import Template

app = Flask(__name__)
@app.route('/',methods=['GET'])
def home():

    events = table.find().sort([('sequence', -1)]).sort([('fraud_probability', -1)]).limit(50)

    # render the template and pass the events
    return render_template('second_home.html', data=events)


@app.route("/line_chart")
def line_chart():
    legend = 'Temperatures'
    temperatures = [73.7, 73.4, 73.8, 72.8, 68.7, 65.2,
                    61.8, 58.7, 58.2, 58.3, 60.5, 65.7,
                    70.2, 71.4, 71.2, 70.9, 71.3, 71.1]
    times = ['12:00PM', '12:10PM', '12:20PM', '12:30PM', '12:40PM', '12:50PM',
             '1:00PM', '1:10PM', '1:20PM', '1:30PM', '1:40PM', '1:50PM',
             '2:00PM', '2:10PM', '2:20PM', '2:30PM', '2:40PM', '2:50PM']
    return render_template('line_chart.html', values=temperatures, labels=times, legend=legend)

# def home():
#     return ''' <p> nothing here, friend but a link to
#                    <a href="/hello">hello</a> and an 
#                    <a href="/form_example">example form</a>
#                    <a href="/simple_chart"> also a simple chart</a>
#                    <a href="/line_chart"> maybe line chart</a></p> '''

# @app.route('/hello', methods=['GET'])
# def hello_word():
#     return ''' <h1> Hello, World!</h1> '''

# @app.route('/form_example', methods=['GET'])
# def form_display():
#     return ''' <form action="/string_reverse" method="POST">
#                 <input type="text" name="some_string" />
#                 <input type="submit" />
#                </form>
#              '''

# @app.route('/string_reverse', methods=['POST'])
# def reverse_string():
#     text=str(request.form['some_string'])
#     reversed_string = text[-1::-1]
#     return ''' output: {}   '''.format(reversed_string)

# @app.route("/simple_chart")
# def chart():
#     legend = 'Monthly Data'
#     labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
#     values = [10, 9, 8, 7, 6, 4, 7, 8]
#     return render_template('chart.html', values=values, labels=labels, legend=legend)

 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)