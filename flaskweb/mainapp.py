#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys

from flask import Flask, request, render_template, send_file
from flask_cors import CORS



app = Flask(__name__, static_folder="static", static_url_path="/")
CORS(app)

mysqlName = "hometest"

########## Test Black ##################################################
@app.route("/")
def routeMain():
    print("routeMain")
    return "<h1>Hello , This a Restful Api Server by Flask...</h1>"
    
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

########## Journeysgo Black ##################################################

########## iDiving Black ##################################################


########## main Black ##################################################
if __name__ == "__main__":
    print(" ")
    port = int(os.environ.get('PORT', 5836))
    #print("port : " + str(port))
    app.run(host='0.0.0.0', port=port, debug=True)
    #server = pywsgi.WSGIServer( ('0.0.0.0', 8336 ), app )
    #server.serve_forever()
    #
    #app.run(host='0.0.0.0', port=port,debug=True)
    
    