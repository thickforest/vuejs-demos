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

def init_api(app):

	@app.route('/')
	def hello_world():
		return 'Hello World!'

	@app.route('/user', methods = ['POST'])
	def addUser():
		print request.json
		username = request.json.get('username')
		password = request.json.get('password')
		print username, password
		user = User()
		user.username = username
		user.password = password
		user.save()
		time.sleep(5)
		return jsonify(trueReturn({'id':user.id}))

	@app.route('/user/<int:userid>', methods = ['DELETE'])
	def delUser(userid):
		print userid
		User.query.filter_by(id=userid).delete()
		session_commit()
		return jsonify(trueReturn({'id':userid}))

	@app.route('/user', methods = ['GET'])
	def getUsers():
		users = User.query.all()
		output = []
		for user in users:
			output.append({'id':user.id, 'username':user.username, 'password':user.password})
		return jsonify(trueReturn(output))
