from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")


@app.route("/googlec935ff44bf4fedc0.html")
def google():
	return render_template("googlec935ff44bf4fedc0.html")


if __name__ == "__main__":
	app.run(debug=False, host="0.0.0.0")
