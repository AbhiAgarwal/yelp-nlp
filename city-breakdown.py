# -*- coding: utf-8 -*-
import argparse, collections, os, csv, sys, locale
import simplejson as json

if __name__ == '__main__':
	stateNeeded = 'NV'
	reviewFile = './yelp-' + stateNeeded + '/0.json'
	businessFile = './yelp-' + stateNeeded + '/business.json'

	reviewData = []
	with open(reviewFile) as f:
		for line in f:
			reviewData.append(json.loads(line))
	reviewData = reviewData[0]
	
	businessData = []
	with open(businessFile) as f:
		for line in f:
			businessData.append(json.loads(line))
	businessData = businessData[0]

	businessCityIDs = []
	businessCityValue = {}
	for i in businessData:
		if i['city'] == 'Las Vegas':
			businessCityIDs.append(i['business_id'])
			businessCityValue[i['business_id']] = i

	reviewCityValue = []
	for i in reviewData:
		reviewBusinessID = i['business_id']
		if reviewBusinessID in businessCityIDs:
			reviewCityValue.append(i)