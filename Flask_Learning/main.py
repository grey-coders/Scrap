from flask import Flask, redirect, render_template, url_for, session

app = Flask(__name__)
app.secret_key = 'aidoafou2859285bhid0q230-923-r89-'

@app.route('/')
def home():
	return render_template('home.html')

if __name__ == '__main__':
	app.run(debug=True)