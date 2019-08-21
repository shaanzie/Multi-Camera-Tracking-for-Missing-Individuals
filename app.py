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

@app.route('/api/v1/tagged',methods=['POST'])
def tagimage():
    global tagData
    tagData=flask.request.json('tagdata')
    cluster=flask.request.json('cluster')
    #run image stuff here
    url = "http://localhost:8000/api/v1/find"
    #read json file for other cameras in cluster
    data={'cluster':cluster}
    r=requests.post(url,data)
    return flask.Response(status=200)
@app.route('/api/v1/imageproc',methods=['POST'])
def imageproc():
    global tagData
    filepath=flask.request.json('filepath')
    #run image stuff here again
    #find which side of frame, read cluster id from setup.json
    url = "http://localhost:8000/api/v1/find"
    data={'cluster':cluster}
    r=requests.post(url,data)
    return flask.Response(status=200)
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)
