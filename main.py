from flask import Flask, render_template, request
from cloudscraper import CloudScraper
import bs4

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
	if request.method == "GET":
		return render_template("index.html", show_tutorial=True)

	link = request.form['url']
	sc = CloudScraper()
	res = sc.get(link)
	soup = bs4.BeautifulSoup(res.content, 'html5lib')
	download_link = soup.find("input", attrs={"type": "hidden", "name": "FU"})
	try:
		download_link = download_link['value']
		return render_template("index.html", show_tutorial=False, download_link=download_link)
	except:
		download_link = "Nan"
		return render_template("index.html", show_tutorial=False, download_link=download_link)



if __name__ == "__main__":
	app.run(debug=False, host="0.0.0.0")
