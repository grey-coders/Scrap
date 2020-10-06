from flask import Flask, redirect, url_for, render_template, session, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key='fayigfoisa974t39465374e936yty894837374890t589367937586739'


@app.route('/')
def home():
	return render_template('home.html')


@app.route('/user', methods=['POST', 'GET'])
def user():
        if 'email' in session:
                return session['email']
        else:
                if request.method == 'POST':
                        session['email'] = request.form['emailid']
                        session['password'] = request.form['password']
                        return session['email']
                else:
                        return redirect(url_for('home'))

@app.route('/logout')
def logout():
	session.pop('email')
	session.pop('password')
	return redirect(url_for('home'))

if __name__ == '__main__':
	app.run(debug=True)
