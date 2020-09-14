import os
import json
import requests
from flask import Flask, render_template, url_for, request


Upload = 'D:\\Flask\\Assignment 2'
app = Flask(__name__)
app.config['uploadFolder'] = Upload






@app.route("/")
def index():
	return render_template("Index.html")

@app.route("/upload", methods = ['POST', 'GET'])
def upload():
	"""
	Takes the image from the user
	and sends that to the rest api
	and gets the image name height and width
	"""
	file = request.files['imgfile']

	filename = file.filename
	file.save(os.path.join(app.config['uploadFolder'], file.filename))
	files = {'image': open(filename, 'rb')}
	url = "http://127.0.0.1:4555/image"
	response = requests.request("POST", url, files=files)
	try:
		jsonfile = response.json()
	except:
		json_data = {
		"name" : "Not supported"
		}
		jsonfile = json.dumps(json_data)

		
	return render_template('index.html', json_data = jsonfile) 




if __name__ == "__main__":
	app.run(debug = True)