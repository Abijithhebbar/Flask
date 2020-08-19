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

class upload(Resource):
    def post(self):
        file = request.files.get('imagefile', '')
        print(request)
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['uploadFolder'], file.filename))
            img = Image.open(file)
            li = []
            li = img.size
            imgobj = {
            "Name" : filename,
            "Height" : li[1],
            "Width" : li[0]
            }
            return jsonify(imgobj)
        else:
            return "Not an image file"


class display(Resource):
    def get(self, fname):
        try:

            img = Image.open(fname)
            li = []
            li = img.size
            imgobj = {
            "Name" : fname,
            "Height" : li[1],
            "Width" : li[0]
            }
            return jsonify(imgobj)
        except :
            return "Filenot found"


api.add_resource(upload, "/image", methods = ['POST'])
api.add_resource(display, '/image/<string:fname>') 
if __name__ == '__main__':
    app.run(debug=True, port = 4555)