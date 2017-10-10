from flask import Flask, redirect, render_template, session, request

app = Flask(__name__)
app.secret_key = 'countup'

@app.route('/')
def index():
	if 'counter' not in session:
		session['counter'] = 0
	return render_template('index.html', counter = session['counter'])

@app.route('/addCount')
def addCount():
	session['counter'] += 1
	print('hello')
	return redirect('/')

app.run(debug=True)