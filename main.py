from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return "<h1>Successfully setup flask in python anywhere</h1>"


if __name__ == "__main__":
	app.run(debug=False, host="0.0.0.0")
