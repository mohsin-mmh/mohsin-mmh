from flask import Flask, render_template, request
from wrangling_scripts.wrangle_data import graph1, graph2, graph3, graph4, date_list
 
app = Flask(__name__)

class DataStore():
    dates=None
    DateSelected=None
    first_graph= None
data=DataStore()

@app.route('/', methods=["GET","POST"])
def home():
    dates = date_list()
    DateSelected = request.form.get('dates', '2021-01-30')
    first_graph = graph1(DateSelected)
    data.DateSelected = DateSelected
    data.first_graph = first_graph
    data.dates = dates
    return render_template('amchart.html', dates=dates, first_graph=first_graph)

@app.route('/result', methods=["GET","POST"])
def returnData():
    result = data.first_graph
    dates = data.dates
    return render_template('amchart_result.html', dates=dates, result=result)


if __name__ == "__main__":
	app.run(debug = True)

