from flask import Flask, render_template
 
app = Flask(__name__)

@app.route('/')
def home():
    data = [
        ("01-07-2021", 1000),
        ("02-07-2021", 700),
        ("03-07-2021", 2000),
        ("04-07-2021", 1500),
        ("05-07-2021", 2200),
        ("05-07-2021", 953),
        ("05-07-2021", 1450),
        ("05-07-2021", 2034),
        ("05-07-2021", 1366),
        ("05-07-2021", 756),
    ]
    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template('graph.html', labels=labels, values=values) 


if __name__ == "__main__":
	app.run(debug = True)

