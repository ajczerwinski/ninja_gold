from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key="SecretKeyMePls"
@app.route('/')
def index():
	try:
		session['gold']
	except:
		session['gold'] = 0
	return render_template("index.html")
@app.route('/process_money', methods=["POST"])
def process_money():
	if request.form["building"] == "Farm":
		session['gold'] = random.randrange(10, 21)
		time_stamp = datetime.now()
		return redirect('/')
	elif request.form["building"] == "Cave":
		session['gold'] = random.randrange(5, 11)
		return redirect('/')
	elif request.form["building"] == "House":
		session['gold'] = random.randrange(2, 6)
		return redirect('/')
	elif request.form["building"] == "Casino":
		session['gold'] = random.randrange(-50, 51)
		return redirect('/')
		# Add/Subtract the right thing

app.run(debug=True)