# -*- coding: utf-8 -*-
import argparse, collections, os, csv, sys, locale
import simplejson as json

if __name__ == '__main__':
	user_json_file = './yelp/yelp_academic_dataset_user.json'
	review_json_file = './yelp/yelp_academic_dataset_review.json'

	userData = []
	with open(user_json_file) as f:
		for line in f:
			userData.append(json.loads(line))

	userHashMap = {}
	for i in userData:
		userID = i['user_id']
		userHashMap[userID] = i

	reviewData = []
	with open(review_json_file) as f:
		for line in f:
			reviewData.append(json.loads(line))

	for i in reviewData:
		reviewUser = i['user_id']
		if userHashMap[reviewUser]:
			if 'userReviews' in userHashMap[reviewUser]:
				userHashMap[reviewUser]['userReviews'].append(i)
			else:
				userHashMap[reviewUser]['userReviews'] = []
				userHashMap[reviewUser]['userReviews'].append(i)

	subset = {}
	currentCount = 0
	for i in userHashMap.keys():
		if currentCount < 1000:
			subset[i] = userHashMap[i]
			currentCount += 1
	with open('./yelp-user/user_1000.json', 'w') as outfile:
		json.dump(subset, outfile)