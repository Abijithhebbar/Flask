import os
import json
import requests
from flask import Flask, render_template, url_for, request, redirect, jsonify
from PIL import Image


Upload = 'static/upload'
app = Flask(__name__)
app.config['uploadFolder'] = Upload


@app.route("/")
def index():
	return render_template("Index.html")

@app.route("/upload", methods = ['POST', 'GET'])
def upload():
	jsonfile = []
	filenames = []
	uploaded_files = request.files.getlist("file[]")
	for file in uploaded_files:
		filename = file.filename
		file.save(os.path.join(app.config['uploadFolder'], file.filename))
		downloadpath = "D:\\Flask\\Assignment 3\\static\\upload"
		os.chdir(downloadpath)
		files = {'image': open(filename, 'rb')}
		url = "http://127.0.0.1:4555/image"
		response = requests.request("POST", url, files=files)
		jsonfile.append(response.json())
		filenames.append(filename)
		normalpath = "D:\\Flask\\Assignment 3"
		os.chdir(normalpath)
	print(filenames)
	return render_template('index1.html', json_data = jsonfile, filename = filenames) 




if __name__ == "__main__":
	app.run(debug = True, port = 9988)

