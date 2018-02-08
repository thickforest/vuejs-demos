#!/usr/bin/python
#coding:utf-8
########################################################################
# File Name: test_migrate.py
# Author: forest
# Mail: thickforest@126.com 
# Created Time: 2018年02月08日 星期四 08时58分57秒
########################################################################

from flask import Flask, request
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)
app.config.from_object('config')
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	if request.method == 'OPTIONS':
		response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
		headers = request.headers.get('Access-Control-Request-Headers')
		if headers:
			response.headers['Access-Control-Allow-Headers'] = headers
	return response

import apis
apis.init_api(app)

from ext import db
db.init_app(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()
