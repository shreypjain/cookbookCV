from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def func():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "no files found"
        elif request.files['files']:
            return "no file uploaded, or wrong name constraint"
        #img is the file for the image that is sent in a request from the front end
        img = request.files['image']
        #general error handling for our program
        return {
            'success': True,
            'message': img
        }
        #the return statement of the machine learning and web scraping will go up there^
        #I will implement a try catch later

