import json as js
import plotly as plt
import plotly.express as px
from flask import Flask, render_template
from wrangling_scripts.wrangle_data import return_table, return_graph1, fig2
 
app = Flask(__name__)


@app.route('/')
def table():
    headings = ("Country","Year","Hectaresarablelandperperson")
    table = return_table()
    data1 = return_graph1()
    data2 = js.dumps(fig2(), cls=plt.utils.PlotlyJSONEncoder)
    country = [row[0] for row in data1]
    values = [row[1] for row in data1]
    return render_template('index.html', headings=headings, data=table, labels=country, values=values, data2=data2)

if __name__ == "__main__":
	app.run(debug = True)


