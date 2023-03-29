from flask import Flask, jsonify, request, render_template
import requests
import base64
app = Flask(__name__)

@app.route("/",methods = ['POST','GET'])
def hello():
  if request.method == 'POST':
    image = request.files['video'].read()
    vid_to_text(image)
    print(image)
    return render_template('home.html')
  else:
    return render_template('home.html')

def vid_to_text(x):  
    
    file_data_base64 = base64.b64encode(x).decode('utf-8')

    response = requests.post(
        "https://rimi98-online-class.hf.space/run/predict", 
        json={
                "data": [
                    {"name": "video.mp4", "data": file_data_base64},
                    file_data_base64
                    ]}
    ).json()
    
    for x in response["data"]:
        print(x[0])
    


if __name__ == '__main__':
  app.run()