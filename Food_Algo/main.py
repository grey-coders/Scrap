from flask import Flask, redirect, session, url_for, render_template

app = Flask(__name__)
@app.route('/')

def home():
	return render_template('food_appender.html')

if __name__ == '__main__':
	app.run(debug=True)