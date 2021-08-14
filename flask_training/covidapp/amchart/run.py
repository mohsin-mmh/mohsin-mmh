from flask import Flask, render_template, request, redirect, url_for
from wrangling_scripts.wrangle_data import graph1, graph2, graph3, graph4, date_list
 
app = Flask(__name__)

class DataStore():
    dates=None
    DateSelected=None
    first_graph= None
    second_graph= None
data = DataStore()

first_graph = graph1(data.DateSelected)
second_graph = graph2(data.DateSelected)
data.first_graph = first_graph
data.second_graph = second_graph

@app.route('/', methods=["GET","POST"])
def home():
    dates = date_list()
    data.dates = dates
    return render_template('amchart.html', dates=dates, dateselected=data.DateSelected)

@app.route('/result', methods=["GET","POST"])
def returnData():
    dates = data.dates
    if request.method == 'POST':
        dateselected = request.form.get('selectdate')
        data.DateSelected = dateselected
        result1 = graph1(dateselected)
        result2 = graph2(dateselected)
        return render_template('amchart_result.html', dates=dates, dateselected=data.DateSelected, result1=result1, result2=result2)

print(data.DateSelected)

#https://stackoverflow.com/questions/64718521/how-to-get-date-from-dropdown-in-flask-and-pass-it-as-an-argument-in-a-function

if __name__ == "__main__":
	app.run(debug = True)