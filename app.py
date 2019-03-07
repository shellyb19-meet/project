from flask import Flask, request, redirect, url_for
from flask import render_template
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def home():
	events=get_upcoming()
	week=get_week_story()
	stories=get_all_stories()
	return render_template("home.html", events=events, week=week, story=story)

if __name__ == '__main__':
	app.run(debug=True)
