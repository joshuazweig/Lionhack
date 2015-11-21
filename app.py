# # #HEROKU STUFF
from flask import Flask, render_template, request, send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask import jsonify
from flask import json
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
import json as simplejson
from decimal import *
import os.path
import csv
import sys
import logging
from datetime import timedelta


from flask.ext.heroku import Heroku

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ergahtoncxgrou:kFgf7Y9hEYIC1DS2oqBqjpWRWy@ec2-54-225-192-128.compute-1.amazonaws.com:5432/d2jua3sn9jr8ng' #hackathon posting secrets shhhhh
#app.config['UPLOAD_FOLDER'] #you prob need to do something about this in heroku#############################
#app.config.from_object(os.environ['APP_SETTINGS'])
heroku = Heroku(app)
db = SQLAlchemy(app)

#######################################################

# from flask import Flask, render_template, request, send_from_directory
# from flask.ext.sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import func
# from flask import jsonify
# from flask import json
# from datetime import datetime
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.sql import text
# import json as simplejson
# from decimal import *
# import os.path
# import csv
# from datetime import timedelta


# app = Flask(__name__, static_url_path='')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/lions_tracks'
# #app.config['UPLOAD_FOLDER'] #you prob need to do something about this in heroku
# db = SQLAlchemy(app)

######LOCALHOST^^^######################################


# Create our database model
class Entry(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    questionId = db.Column(db.String(10)) #assign Ids for vote and each question in survey 
    trump = db.Column(db.Integer) #number of votes for each entry
    carson = db.Column(db.Integer)
    rubio = db.Column(db.Integer)
    cruz = db.Column(db.Integer)
    bush = db.Column(db.Integer)
    christie = db.Column(db.Integer)
    paul = db.Column(db.Integer)
    kasich = db.Column(db.Integer)

    def __init__(self, questionId, trump, carson, rubio, cruz, bush, christie, paul, kasich):
        self.questionId = questionId
        self.trump = trump
        self.carson = carson
        self.rubio = rubio
        self.cruz = cruz
        self.bush = bush
        self.christie = christie
        self.paul = paul
        self.kasich = kasich

# Set "homepage" to index.html
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update():
    questionId = request.form['questionId'] 
    trump = request.form['trump']
    carson = request.form['carson']
    rubio = request.form['rubio']
    cruz = request.form['cruz']
    bush = request.form['bush']
    christie = request.form['christie']
    paul = request.form['paul']
    kasich = request.form['kasich']

    if request.method == 'POST':
        e = Entry(questionId, trump, carson, rubio, cruz, bush, christie, paul, kasich)
        db.session.add(e)
        db.session.flush()

    db.session.commit()
    return 'success'


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")