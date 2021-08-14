from flask import Flask, render_template
from wrangling_scripts.wrangle_data import graph1, graph2, graph3, graph4, date_list
 
app = Flask(__name__)


@app.route('/')
def home():
    dates = date_list()
    date_choosen = '2020-09-23'
    first_graph = graph1(date_choosen)
    second_graph = graph2(date_choosen)
    third_graph = graph3(date_choosen)
    fourth_graph = graph4(date_choosen)
    country1 = [row[0] for row in first_graph]
    values1 = [row[1] for row in first_graph]
    country2 = [row[0] for row in second_graph]
    values2 = [row[1] for row in second_graph]
    country3 = [row[0] for row in third_graph]
    values3 = [row[1] for row in third_graph]
    country4 = [row[0] for row in fourth_graph]
    values4 = [row[1] for row in fourth_graph]

    return render_template('graph.html', dates=dates, labels1=country1, values1=values1, labels2=country2, values2=values2, labels3=country3, values3=values3, labels4=country4, values4=values4)

if __name__ == "__main__":
	app.run(debug = True)

