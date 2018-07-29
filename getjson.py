#!/usr/bin/python

import json
import requests

def getPrice(coin):
	url = 'https://api.coinmarketcap.com/v2/ticker/'
	data = requests.get(url).content
	output = json.loads(data)
	price = 0
	for i in range(0, 100):
		if (list(output['data'].items())[i][1]['website_slug'].lower() == coin.lower()):
			price = list(output['data'].items())[i][1]['quotes']['USD']['price']
			break
				
	if(price == 0):
		for i in range(0, 100):
			if (list(output['data'].items())[i][1]['symbol'].lower() == coin.lower()):
				price = list(output['data'].items())[i][1]['quotes']['USD']['price']
				break
	return price
				
#print(getPrice("bitcoin"))
#print(getPrice("litecoin"))
#print(getPrice("dogecoin"))
#print(getPrice("AELDS") == 0)

	
