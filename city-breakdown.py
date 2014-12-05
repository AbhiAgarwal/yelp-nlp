# -*- coding: utf-8 -*-
import argparse, collections, os, csv, sys, locale
import simplejson as json

if __name__ == '__main__':
	stateNeeded = 'NV'
	reviewFile = './yelp-' + stateNeeded + '/0.json'
	businessFile = './yelp-' + stateNeeded + '/business.json'
	userFile = './yelp/yelp_academic_dataset_user.json'

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

	userData = []
	with open(userFile) as f:
		for line in f:
			userData.append(json.loads(line))

	# FORMATTING DATA

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

	userValue = {}
	for i in userData:
		userValue[i['user_id']] = i

	# Formation of CSV file
	for i in reviewCityValue:
		currentBusiness = businessCityValue[i['business_id']]
		currentUser = userValue[i['user_id']]

		i['latitude'] = currentBusiness['latitude']
		i['longitude'] = currentBusiness['longitude']
		i['business_stars'] = i['stars']
		i['review_stars'] = currentBusiness['stars']
		i['sentiment'] = 0
		i['review_count'] = currentUser['review_count']
		i['average_stars'] = currentUser['average_stars']
		i['yelping_since'] = currentUser['yelping_since']
		i['user_votes'] = currentUser['votes']
		i['fans'] = currentUser['fans']

		del i['user_id']
		del i['type']
		del i['date']
		del i['business_id']

	with open('./yelp-' + stateNeeded + '/review.json', 'w') as outfile:
		json.dump(reviewCityValue, outfile)