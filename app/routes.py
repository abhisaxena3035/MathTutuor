from flask import render_template
from app import app 

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title='Home')

@app.route('/algebra')
def algebra():
	return render_template('algebra.html', title='Algebra')

@app.route('/geometery')
def geometery():
	return render_template('geometery.html', title='Geometery')

@app.route('/calculus')
def calculus():
	return render_template('calculus.html', title='Calculus')


