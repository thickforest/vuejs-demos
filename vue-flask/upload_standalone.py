#!/usr/bin/python
#coding:utf-8
from flask import Flask, request, jsonify, make_response
from common import *
app = Flask(__name__)
app.debug = True

@app.route('/upload', methods=['POST'])
def upload():
	error = None
	if request.method == 'POST':
		f = request.files['filename']
		if f.filename.split('.')[-1] in ['jpg', 'jpeg', 'png', 'gif']:
			if not os.path.exists('images'):
				os.mkdir('images')
			f.save('images/' + f.filename)
			return jsonify(trueReturn({'url':'http://192.168.123.33:5000/images/' + f.filename}))
		else:
			error = u'非法图片'
	return jsonify(falseReturn({'msg':error}))

@app.route('/images/<string:filename>', methods=['GET'])
def download(filename):
	print 'download:', filename
	content = open('images/' + filename).read()
	response = make_response(content)
	response.headers['Content-Disposition'] = 'attachment; filename=' + filename
	return response

@app.route('/')
def index():
	return 'Index Page'

@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	if request.method == 'OPTIONS':
		response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
		headers = request.headers.get('Access-Control-Request-Headers')
		if headers:
			response.headers['Access-Control-Allow-Headers'] = headers
	return response

if __name__ == '__main__':
	app.run(host = '0.0.0.0')
