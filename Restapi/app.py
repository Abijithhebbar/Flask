#!flask/bin/python
import os
import json
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from PIL import Image


Upload = '/Flask/Restapi'
app = Flask(__name__)
app.config['uploadFolder'] = Upload
api = Api(app)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def imgjson(file):
	img = Image.open(file)
	width, height = img.size
	imgobj = {
	"Name": file.filename,
	"Width" : width,
	"Height" : height
	}
	return imgobj

class upload(Resource):
    def post(self):
        file = request.files.get('imagefile', '')
        print(request)
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['uploadFolder'], file.filename))
            return jsonify(imgjson(file))
        else:
            return "Not an image file"


class display(Resource):
    def get(self, fname):
        try:

            img = Image.open(fname)
            width, height = img.size
            imgobj = {
            "Name" : fname,
            "Height" : height,
            "Width" : width
            }
            return jsonify(imgobj)
        except :
            return "Filenot found"


api.add_resource(upload, "/image", methods = ['POST'])
api.add_resource(display, '/image/<string:fname>') 
if __name__ == '__main__':
    app.run(debug=True, port = 4555)