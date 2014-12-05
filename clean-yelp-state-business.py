# -*- coding: utf-8 -*-
import argparse, collections, os, csv, sys, locale
import simplejson as json

if __name__ == '__main__':
	stateNeeded = 'ON'
	business_json_file = './yelp/yelp_academic_dataset_business.json'

	businessData = []
	with open(business_json_file) as f:
		for line in f:
			businessData.append(json.loads(line))
	state = []
	for i in businessData:
		key = i['state']
		if key == stateNeeded:
			state.append(i)
	with open('./yelp-' + stateNeeded + '/business.json', 'w') as outfile:
		json.dump(state, outfile)