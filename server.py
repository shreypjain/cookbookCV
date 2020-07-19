from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def func():
    if request.method == 'POST':
        output = []
        if 'file' not in request.files:
            return "no files found"
        elif request.files['files']:
            return "no file uploaded, or wrong name constraint"
        #img is the file for the image that is sent in a request from the front end
        img = request.files['image']
        

if __name__ == "__main__":
    app.run(debug=True,port=8000)

