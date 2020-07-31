from flask import Flask, request
from werkzeug.utils import secure_filename
import os, socket

host = socket.gethostname()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'img'

@app.route('/', methods=['GET','POST'])
def func():
    if request.method == 'POST':
        img = request.files['image']
        filename = secure_filename('img.jpg')
        var = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        img.save(var)
        return("happened")
    else:
        return '''<div class="container">
  <div class="row">
    <div class="col">
      <h1>Upload an image</h1>
      <hr>
      <form action="/" method="POST" enctype="multipart/form-data">
        <div class="form-group">
          <label>Select image</label>
          <div class="custom-file">
            <input type="file" class="custom-file-input" name="image" id="image">
            <label class="custom-file-label" for="image">Select image...</label>
          </div>
        </div>
        <button type="submit" class="btn btn-primary">Upload</button>
      </form>
    </div>
  </div>
</div>'''

if __name__ == "__main__":
    app.debug = True
    ip = socket.gethostbyname(host)
    app.run(host=ip, port=8000)

