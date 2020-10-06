from flask import Flask, render_template, sessions, request


app = Flask(__name__)

@app.route('/')

def home():
	return render_template('home.html')

@app.route('/calculator', methods=['POST', 'GET'])

def calculator():
	if request.method =='POST':
	        data = request.form['series']
	        return f"hello!{data}"
	else:
		return render_template('home.html')
if __name__ == "__main__":
	app.run(debug=True)
