from flask import Flask, redirect, url_for, render_template, session, request, flash
import pyautogui as py
from time import sleep

app = Flask(__name__)
app.secret_key='aiohfoi83768403289fh;fh;df'
@app.route('/')
def home():
	
	return render_template('home.html')

@app.route('/find', methods=['POST', 'GET'])
def find():
	if request.method == 'POST':
		if not'time' in session:
				try:
				  	session['time'] = request.form['time']
				  	sleep(int(session['time']))
				  	flash(str(py.position()), 'danger')
				  	session.pop('time', None)
				  	return redirect(url_for('home'))
				except:
					session.pop('time', None)
					return redirect(url_for('home'))
		else:
			session.pop('time', None)
			return redirect(url_for('home'))
	else:
		session.pop('time', None)
		return redirect(url_for('home'))
if __name__ == '__main__':
	app.run(debug=True)
