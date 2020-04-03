from flask import Flask, render_template,request, redirect, url_for,jsonify
import cv2
import sys
import numpy
import os
import json

#import gesture
app = Flask(__name__)
@app.route('/')
def landing(name=None):
    return render_template('landing.html',name=name)

@app.route('/vote')
def parse(name=None):
    import face_recognize
    print("done")
    return render_template('index.html',name=name)

# @app.route('/speech')
# def spech():
#     control = speech.call()
#     print(control)
#     with open('control.json', 'w') as fp:
#         json.dump(control,fp)
#     return jsonify(control)
#     #return render_template('blind.html')

@app.route('/api')
def api():
    with open('control.json','r') as fp:
        return jsonify(json.load(fp))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')