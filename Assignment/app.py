import os
import json
from flask import Flask, render_template, jsonify, request
from PIL import Image


Upload = 'static/upload'
app = Flask(__name__)
app.config['uploadFolder'] = Upload

"""
Flask app home page
"""
@app.route("/")

def start():
	return render_template("Index.html")

"""
Takes the image from the user.
sends the image to writeToJson method and displays the uploaded image.
"""
@app.route("/upload", methods = ['POST', 'GET'])

def getImage():
	imagefile = request.files['image']
	filename = imagefile.filename
	imagefile.save(os.path.join(app.config['uploadFolder'], filename))
	writeToJson(filename)
	return render_template('index.html', filename = filename)

"""
Is called by getImage method.
get the json data of the image from getData method and writes it to json file.
"""
def writeToJson(imagefile):
	imageobj = getData(imagefile)
	with open('jsonfile.json', 'w') as json_file:
		json.dump(imageobj, json_file)

"""
Is called by writeToJson method.
gets the image name from writeToJson method.
opens the image using the Pillow library and gets the height and width of the image and returns that to writeToJson method.
"""
def getData(imagefile):
	os.chdir("D:\\Flask\\Assignment\\static\\upload")
	img = Image.open(imagefile)
	width, height = img.size
	imgobj = {
	"name" : imagefile,
	"width" : width,
	"height" : height
	}
	os.chdir("D:\\Flask\\Assignment")
	return imgobj



if __name__ == "__main__":
	app.run(debug = True, port = 4455)