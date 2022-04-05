from flask import Flask
from flask import render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle="Home")

@app.route('/about')
def about():
    return render_template('about.html',pageTitle="About")

@app.route('/estimate', methods=['GET', 'POST'])
def estimate():
    if request.method == 'POST': 
        form = request.form
        radius = float(form['radius'])
        height = float(form['height'])
        pi = 3.14
        top = pi * radius * radius
        sides = 2 * pi * (radius * height)
        area = top + sides
        square = area/144
        material_cost = square * 25
        labor_cost = square * 15
        estimate_total = material_cost + labor_cost
        return render_template('estimate.html', calculate=estimate_total)
    return render_template('estimate.html', pageTitle="Estimate")

if __name__ == '__main__':
    app.run(debug=True)