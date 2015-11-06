from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
time = datetime.now()
app = Flask(__name__)
app.secret_key="SecretKeyMePls"
@app.route('/')
def index():
	try:
		session['gold']
	except:
		session['gold'] = 0
	try:
		session['message']
	except:
		session['message'] = []
	return render_template("index.html")
@app.route('/process_money', methods=["POST"])
def process_money():
	if request.form["building"] == "Farm":
		session['farm_gold'] = random.randrange(10, 21)
		session['gold'] += session['farm_gold']
		output = "Earned %d gold from the farm! %s" %(session['farm_gold'], time)
		session['message'].append(output)
		session['building'] = "Farm"
		return redirect('/')
	elif request.form["building"] == "Cave":
		session['cave_gold'] = random.randrange(5, 11)
		session['gold'] += session['cave_gold']
		session['building'] = "Cave"
		return redirect('/')
	elif request.form["building"] == "House":
		session['house_gold'] = random.randrange(2, 6)
		session['gold'] += session['house_gold']
		session['building'] = "House"
		return redirect('/')
	elif request.form["building"] == "Casino":
		session['casino_gold'] = random.randrange(-50, 51)
		session['gold'] += session['casino_gold']
		session['building'] = "Casino"
		return redirect('/')
app.run(debug=True)