from flask import Flask, request, redirect, url_for
from flask import render_template
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def home():
	return render_template("home.html")

if __name__ == '__main__':
	app.run(debug=True)
