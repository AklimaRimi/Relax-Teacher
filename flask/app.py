from flask import Flask, jsonify, request, render_template
import requests
from werkzeug.utils import secure_filename
import base64
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/upload/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = ['mp4']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/",methods = ['POST','GET']) 
def hello():
  if request.method == 'POST':
    image = request.files['video']
    vid = image    
    image.save(f'{UPLOAD_FOLDER}video.mp4')
    # image.close()
    text = ''
    with open(f'{UPLOAD_FOLDER}video.mp4', "rb") as videoFile:
      text = videoFile.read()
  
    data = vid_to_text(text)
    text,summary,label = data['text'], data['summary'],data['label']
    return render_template('uploaded.html',text=text,summary=summary,label=label,video = 'upload/video.mp4')
    # return render_template('home.html')
  else:
    return render_template('home.html')

def vid_to_text(x):  
    
    file_data_base64 = base64.b64encode(x).decode('utf-8')

    response = requests.post("https://rimi98-online-class.hf.space/run/predict",
        json={
                "data": [
                    {"name": "video.mp4", "data": file_data_base64},
                    file_data_base64
                    ]}
    ).json()
    
    return response['data'][0]
    
    # print(response)
  
if __name__ == '__main__':
  app.run()
