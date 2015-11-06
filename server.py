from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key="SecretKeyMePls"
@app.route('/')
def index():
	try:
		session['gold']
	except:
		session['gold'] = 0
	return render_template("index.html")
@app.route('/process_money')
def process_money():
	session['gold'] += 1
app.run(debug=True)