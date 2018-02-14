#!/usr/bin/python
#coding:utf-8
########################################################################
# File Name: models.py
# Author: forest
# Mail: thickforest@126.com 
# Created Time: 2018年02月08日 星期四 10时07分05秒
########################################################################
from ext import db
from sqlalchemy.exc import SQLAlchemyError

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(20))
	password = db.Column(db.String(20))
	age = db.Column(db.Integer)
	login_time = db.Column(db.Integer)
	addresses = db.relationship('Address', backref='user')

	def save(self):
		db.session.add(self)
		return session_commit()

	def delete(self):
		db.session.delete(self)
		return session_commit()
		

class Address(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	email_address = db.Column(db.String(50))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


def session_commit():
	try:
		db.session.commit()
	except SQLAlchemyError as e:
		db.session.rollback()
		reason = str(e)
		return reason
