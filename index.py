#!/usr/bin/python

import os
import requests
import json
from flask import Flask, request
from getjson import getPrice
token = os.environ.get('FB_ACCESS_TOKEN')
mytoken = os.environ.get('FB_VERIFY_TOKEN')
app = Flask(__name__)
initialMessage = "Hello! I'm a bot created to show you any criptocurrency price you want. You only need to enter the name of the coin preceded by @. Example: @bitcoin."  
def sendMessage(sender, message):
	payload = {'recipient': {'id': sender}, 'message': {'text': message}}
	r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)
	
@app.route('/', methods=['GET', 'POST'])
def webhook():
	if request.method == 'POST':
		try:
			data = json.loads(request.data.decode())
			text = data['entry'][0]['messaging'][0]['message']['text']
			print(text)
			sender = data['entry'][0]['messaging'][0]['sender']['id']
			if(text[0] == '@'):
				sendMessage(sender, getPrice(text[1:]))
				print(getPrice(text[1:]))
			else:
				sendMessage(sender, initialMessage)
		except Exception as e:
			print(traceback.format_exc())

	elif request.method == 'GET':
		if request.args.get('hub.verify_token') == os.environ.get(mytoken):
			return request.args.get('hub.challenge')
		return "Wrong Verify Token"
	return "Nothing"

if __name__ == '__main__':
	app.run(debug=True)
