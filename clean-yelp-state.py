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
	json_file = './yelp/yelp_academic_dataset_business.json'
	csv_file = './yelp/yelp_academic_dataset_business.csv'
	csv_file_removed = './yelp/yelp_academic_dataset_business_1.csv'
	data = []
	with open('./yelp/yelp_academic_dataset_business.json') as f:
		for line in f:
			data.append(json.loads(line))
	state = []
	for i in data:
		key = i['state']
		if key == stateNeeded:
			state.append(i)
	with open('./yelp-' + stateNeeded + '/business.json', 'w') as outfile:
		json.dump(state, outfile)