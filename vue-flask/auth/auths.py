#!/usr/bin/python
#coding:utf-8
########################################################################
# File Name: auth/apis.py
# Author: forest
# Mail: thickforest@126.com 
# Created Time: 2018年02月15日 星期四 01时28分25秒
########################################################################
from flask_jwt import JWT
from users.models import User, session_commit
import config
import common
import time

# 用户登录接口已由flask_jwt默认定义好，默认路由是"/auth"，可以在配置文件中配置:
# JWT_AUTH_URL_RULE = '/login'
# 需要注意的是，登录接口的传值要使用 application/json 形式
# >>> curl -i -H 'Content-Type: application/json' http://192.168.123.33:5000/login -d '{"username":"hurui", "password":"66666"}
# {
#   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MTksImlhdCI6MTUxODY0MjIwOSwibmJmIjoxNTE4NjQyMjA5LCJleHAiOjE1MTg2NDI1MDl9.iwbRXyCXsqHxpySxGTQQ1nvogH_PCRfJ-w0SC7htNGs"
# }

def authenticate(username, password):
	print 'authenticating:', username, password
	userInfo = User.query.filter_by(username = username).first()
	if (userInfo is None):
		return 'error: username can not found!', 400
		self.error_handler('找不到用户')
	else:
		# if (Users.check_password(Users, userInfo.password, password)):
		if (userInfo.password == password):
			login_time = int(time.time())
			userInfo.login_time = login_time
			session_commit()
			return userInfo
		else:
			return 'error: password incorrect!', 400

# >>> curl -i -H "Authorization: jwt eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MTksImlhdCI6MTUxODY0MjIwOSwibmJmIjoxNTE4NjQyMjA5LCJleHAiOjE1MTg2NDI1MDl9.iwbRXyCXsqHxpySxGTQQ1nvogH_PCRfJ-w0SC7htNGs" http://192.168.123.33:5000/user/secret
# HTTP/1.0 401 UNAUTHORIZED
# {
#  "description": "Signature has expired", 
#  "error": "Invalid token", 
#  "status_code": 401
# }

def identity(payload):
	print 'identity:', payload	# {u'iat': 1518642209, u'exp': 1518642509, u'nbf': 1518642209, u'identity': 19}
	_id = payload['identity']
	print 'Iat', time.ctime(payload['iat'])
	print 'Now:', time.ctime()
	print 'Exp:', time.ctime(payload['exp'])
	return User.query.filter_by(id = _id).first()
