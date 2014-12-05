"""
Cleaning Yelp dataset
    1. Taking JSON and converting it to CSV
    2. Removing type, business_id, user_id, date

"""

# -*- coding: utf-8 -*-
import argparse, collections, os, csv, sys, locale
import simplejson as json

if __name__ == '__main__':
	stateNeeded = 'NY'
	business_json_file = './yelp-' + stateNeeded + '/business.json'
	review_json_file = './yelp/yelp_academic_dataset_review.json'

	businessData = []
	with open(business_json_file) as f:
		for line in f:
			businessData.append(json.loads(line))
	allIDs = []
	for i in businessData[0]:
		allIDs.append(i['business_id'])

	reviewData = []
	with open(review_json_file) as f:
		for line in f:
			reviewData.append(json.loads(line))
	eachStateReviews = []
	for i in reviewData:
		businessID = i['business_id']
		if businessID in allIDs:
			eachStateReviews.append(i)
	with open('./yelp-' + stateNeeded + '/review.json', 'w') as outfile:
		json.dump(eachStateReviews, outfile)