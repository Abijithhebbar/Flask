import os
import json
import requests
from flask import Flask, render_template, request


Upload = 'D:\\Flask\\Assignment 2'
app = Flask(__name__)
app.config['uploadFolder'] = Upload





"""
Flask app home page
"""
@app.route("/")
def start():
	return render_template("Index.html")

@app.route("/upload", methods = ['POST', 'GET'])
def getImage():
	"""
	Takes the image from the user
	and sends that to the rest api
	and gets the image name height and width
	"""
	saveimage = request.files['image']

	imagename = saveimage.filename
	saveimage.save(os.path.join(app.config['uploadFolder'], imagename))
	files = {'image': open(imagename, 'rb')}
	jsonfile = getData(files)		
	return render_template('index.html', json_data = jsonfile) 

"""
takes the files from the getImage sends that to REST API.
gets the data from RESTAPI and returns that to getImage()
"""
def getData(files):
	url = "http://127.0.0.1:4555/image"
	response = requests.request("POST", url, files=files)
	try:
		jsonfile = response.json()
	except:
		json_data = {
		"name" : "Not supported"
		}
		jsonfile = json.dumps(json_data)
	return jsonfile


if __name__ == "__main__":
	app.run(debug = True)