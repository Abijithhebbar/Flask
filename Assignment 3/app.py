import os
import json
import requests
from flask import Flask, render_template, url_for, request, redirect, jsonify
from PIL import Image


Upload = 'static/upload'
app = Flask(__name__)
app.config['uploadFolder'] = Upload

"""
Renders the Home page of the application.
"""
@app.route("/", methods = ['POST', 'GET'])
def index():
	return render_template("Index.html")
"""
It gets the files from the index.html page.
Sends the image to REST API and gets the image height width and image name as json from the REST API.
The Image name height and width are sent to the Index1.html page
where we display the images in a carousel with svg boundaries.
"""
@app.route("/upload", methods = ['POST', 'GET'])
def upload():
	jsonfile = []
	filenames = []
	uploaded_files = request.files.getlist("Imagefiles[]")
	slider_value = request.form["value_of_slider"]
	for file in uploaded_files:
		filename = file.filename
		file.save(os.path.join(app.config['uploadFolder'], file.filename))
		downloadpath = "D:\\Flask\\Assignment 3\\static\\upload"
		os.chdir(downloadpath)
		files = {'image': open(filename, 'rb')}
		url = "http://127.0.0.1:4555/image"
		response = requests.request("POST", url, files = files) # gets the response from the REST API
		jsonfile.append(response.json()) # gets the json output of the response from REST API
		filenames.append(filename)
		normalpath = "D:\\Flask\\Assignment 3"
		os.chdir(normalpath)
	return render_template('index1.html', json_data = jsonfile, filename = filenames, boundary = int(slider_value)) 



if __name__ == "__main__":
	app.run(debug = True, port = 9988)

