"""
########################################
IMPORTING STUFF
########################################
"""

from flask import Flask,render_template,request,g,session
from werkzeug.security import generate_password_hash
import sqlite3
from pytz import timezone
from flask_cachebuster import CacheBuster
from flask_mail import Mail, Message
import math, random
from dbops_usual import *
from logging_ops import clear_logs
from routes import *
from new_routes import *
from config import *
from excelops import *

""""
########################################
TO DO : 
    1 - Commence Testing of strcuture/basic app running with a dummy template
    2 - Add To-do in mailops of all mailtemplates discussed.


STRUCTURES :
    1 - Create seperate file for routes depending on type of requests/operations    (X)
    2 - Create seperate file for excel operations                                   (X)
    3 - Research on running a cron-job to monitor inbox for unread messages.        ( )
        Maybe use the bridge request email to create/trigger an outage.


########################################
"""






"""
########################################
CONFIGURING APP
########################################
"""









"""
########################################
BEFORE AND AFTER REQUEST FUNCTIONS (REQUIRES TESTING)
########################################
"""
@app.before_request
def before_every_request():
    g.db = connect_db()

@app.after_request
def after_every_request(response):
    g.db.close()
    return response




'''
########################################
RUNNING APP
########################################
'''

if _name_ == '_main_':
    #serve(app,url_scheme='https')               --Use this in PROD ONLY
    with app.app_context():
        before_every_request()
        init_db()                               #-- Never use this. This is only for resetting DB. If using it, After reset, Please add admin users manually.
        app.logger.info("Info Testing!")
    app.run(debug=True)