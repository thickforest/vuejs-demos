#!/usr/bin/python
#coding:utf-8
########################################################################
# File Name: common.py
# Author: forest
# Mail: thickforest@126.com 
# Created Time: 2018年02月08日 星期四 10时43分28秒
########################################################################

def trueReturn(data, msg="请求成功"):
	return {
		"status": 1,
		"data": data,
		"msg": msg
	}

def falseReturn(data, msg="请求失败"):
	return {
		"status": 0,
		"data": data,
		"msg": msg
	}
