import os
import json
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
	file = request.files['imgfile']
	filename = file.filename
	file.save(os.path.join(app.config['uploadFolder'], file.filename))
	img = Image.open(file)
	li = []
	li = img.size
	imgobj = {
	"name" : filename,
	"width" : li[0],
	"height" : li[1]
	}
	json_data = json.dumps(imgobj)
	with open('jsonfile.json', 'w') as json_file:
		json.dump(imgobj, json_file)
	print(json_data)
	print(type(json_data))
	return render_template('index.html', filename = filename) # comment this line to only get the json data.
	# return render_template('index.html', json_data = json_data) # uncomment this line to get only json data.




if __name__ == "__main__":
	app.run(debug = True)