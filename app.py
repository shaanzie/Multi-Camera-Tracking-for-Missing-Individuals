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
#1
# @app.route('/api/v1/create',methods= ['POST'])
# def createContract():
#     ''' creates vote contract '''
#     global voteData
#     cid=flask.request.json['candidateid']
#     voteData=cid
#     cid=cid.split()
#     cid=''.join(cid)
#     os.system(r".\\azure-vote\\node_modules\\.bin\\wdio .\\azure-vote\\wdio.conf.js --suite contract "+cid)
#     return flask.Response(status=200)

# @app.route('/api/v1/verify',methods=['GET'])
# def takeaction():
#     ''' does verification '''
#     #profile values send as cli arguments
#     trace=os.popen("python hashing.py").read()
#     ver=os.system(r".\\azure-vote\\node_modules\\.bin\\wdio .\\azure-vote\\wdio.conf.js --suite verify "+trace)
#     if ver!=0:
#         return flask.Response(status=401)
#     else:
#         s = smtplib.SMTP('smtp.gmail.com', 587) 
#         s.starttls() 
#         s.login("anandlagwankerm", "Animesh@Ishaan@Tejvi1234") 
#         message = "Voted for "+voteData
#         s.sendmail("anandlagwankerm@gmail.com", "anandlagwankerm@gmail.com", message) 
#         s.quit() 
#         return flask.Response(status=200)

# @app.route('/api/v1/action',methods=['GET'])
# def verify():
#     ''' verfies whether the vote is valid '''
#     os.system(r".\\azure-vote\\node_modules\\.bin\\wdio .\\azure-vote\\wdio.conf.js --suite action "+ voteData)
#     return flask.Response(status=200)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)
