#!/usr/bin/python
#coding:utf-8
########################################################################
# File Name: main.py
# Author: forest
# Mail: thickforest@126.com 
# Created Time: 2018年02月08日 星期四 09时46分19秒
########################################################################
from flask import jsonify, request
from models import User, Address, session_commit
from common import *
import time
from flask_jwt import jwt_required, current_identity

def init_api(app):

	@app.route('/')
	def hello_world():
		return 'Hello World!'

	@app.route('/user', methods = ['POST'])
	def addUser():
		print 'Add:', request.json
		username = request.json.get('username')
		password = request.json.get('password')
		age = request.json.get('age')
		user = User()
		user.username = username
		user.password = password
		user.age = age
		user.save()
		session_commit()
		return jsonify(trueReturn({'id':user.id}))

	@app.route('/user/<int:userid>', methods = ['DELETE'])
	def delUser(userid):
		print 'Detele:', userid
		User.query.filter_by(id=userid).delete()
		session_commit()
		return jsonify(trueReturn({}))

	@app.route('/user', methods = ['GET'])
	def getUsers():
		users = User.query.all()
		output = []
		for user in users:
			output.append({'id':user.id, 'username':user.username, 'password':user.password, 'age':user.age})
		print 'List:', output
		return jsonify(trueReturn(output))

	@app.route('/user/secret', methods = ['GET'])
	@jwt_required()
	def getUserSecret():
		msg = {'id': current_identity.id}
		return jsonify(trueReturn(msg))
