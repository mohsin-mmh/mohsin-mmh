from flask import Flask, render_template, request, redirect, url_for
from wrangling_scripts.wrangle_data import graph1, graph2, date_list
 
app = Flask(__name__)

class DataStore():
    dates=None
    DateSelected=None
    first_graph= None
    second_graph= None
data = DataStore()

@app.route('/', methods=["GET","POST"])
def home():
    dates = date_list()
    data.dates = dates
    return render_template('amchart.html')

if __name__ == "__main__":
	app.run(debug = True)