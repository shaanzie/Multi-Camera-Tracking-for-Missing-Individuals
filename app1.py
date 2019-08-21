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
