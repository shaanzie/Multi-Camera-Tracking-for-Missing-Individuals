import requests
import flask
import json
import subprocess
import os
from flask_cors import CORS
import threading
import smtplib
app = flask.Flask(__name__)
tagData=''
CORS(app)

@app.route('/api/v1/find',methods=['POST'])
def tagimage():
    label=''
    ip=''
    location=[]
    filepath=[]
    cluster=flask.request.json['cluster']
    with open("setup.json") as json_file:
        data=json.load(json_file)
        for info in data[cluster]:
            label=info['label']
            ip=info['ip']
            #deploy pods to cluster
            for camera in info['cameras']:
                for i in info[camera]:
                    location.append(i[1])
                    filepath.append(i[0])
    json_data={"label":label, "ip":ip, "location": location, "filepath":filepath}
    r=requests.post("http://localhost:5000/api/v1/imageproc",data)
    return flask.Response(status=200)
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8000)
