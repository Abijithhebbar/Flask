#!flask/bin/python
import os
import json
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from PIL import Image


Upload = '/Flask/Restapi' # Setting the path for the downloading Images
app = Flask(__name__) # Creating app module
app.config['uploadFolder'] = Upload
api = Api(app) # Creating api for routing the app module
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

"""
This method is used to check the extension of the uploaded file and if it is an image or not.
"""
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



"""
To return the image name height width as a json
"""

def imgjson(file):
	img = Image.open(file) # Opens the image using Image library
	width, height = img.size # gets the height and width of the image.
	imgobj = {
	"Name": file.filename,
	"Width" : width,
	"Height" : height
	}
	return imgobj
"""
To return the error message
"""
def errormsg(message):
    errorMessage = {
    "Output" : message
    }
    return errorMessage

"""
Upload the file using the post method and display the image height width and name
"""
class upload(Resource):
    """
    Post method to catch the image
    """
    def post(self):
        file = request.files.get('imagefile', '') # used to catch the image from the post
        try: # try except for checking the not allowed formats
            if file and allowed_file(file.filename):
                filename = file.filename
                file.save(os.path.join(app.config['uploadFolder'], file.filename))
                print(file)
                return jsonify(imgjson(file))
            else:
                message = "format not supported"
                return jsonify(errormsg(message)) # prints the error json message
        except:
            pass

"""
Display class to get the image stored in the local
"""
class display(Resource):
    """
    Get method to get the images
    """
    def get(self, fname):
        # Try if the given file name exists
        try:

            img = Image.open(fname) # Opens the Image using the Image library to get the height and width
            width, height = img.size # gets the height and width of the image
            imgobj = {
            "Name" : fname,
            "Height" : height,
            "Width" : width
            }
            return jsonify(imgobj)
        except :
            message = "File not found"
            return  jsonify(errormsg(message))# If the file not found return this


api.add_resource(upload, "/image", methods = ['POST']) # App route for POST method.
api.add_resource(display, '/image/<string:fname>') # App route for GET method.
if __name__ == '__main__':
    app.run(debug=True, port = 4555)