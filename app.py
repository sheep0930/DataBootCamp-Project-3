# import necessary libraries
from flask import Flask, render_template
import econdatapull

#Imports all dependencies
import pandas as pd
import datetime
import json
import requests
from sqlalchemy import create_engine, inspect, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date 
Base = declarative_base()
import sqlite3
from sqlalchemy.orm import Session


# create instance of Flask app
app = Flask(__name__)

# flask route to update database
@app.route("/")
def index():

    return render_template("index.html")


@app.route('/api/update')
def updateAPI():
    API_get.updateDB()
    pass

# hacky way to possibly get the JSON from API_get
# this route is more related to what Yang's doing but I figured I'd put this here
# for test purposes (note that it may not actually work)
# be sure to delete this route (or modify it) to not use updateDB, since this isn't really what the function's for
@app.route('api/get')
def getAPI():
    return jsonify(API_get.updateDB())

if __name__ == '__main__':
    app.run(debug = True)