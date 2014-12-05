import json
businessData = []
with open('review.json') as f:
	for line in f:
		businessData.append(json.loads(line))
len(businessData[0])