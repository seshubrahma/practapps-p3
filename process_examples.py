import json

folder = "example_runs/donald_born/"

nbest = json.loads(open(folder+"nbest_predictions.json").read())
questions = json.loads(open(folder+"newsQuestions.json").read())


probDict = {}

for k in nbest.keys():
	for i in range(len(nbest[k])):
		key = nbest[k][i]['probability']
		probDict[str(key)] = nbest[k][i]['text']

HOW_MANY_TO_PRINT = 10	

print(questions['data'][0]['paragraphs'][0]['qas'][0]['question'])
count = 1
for i in sorted(probDict.keys())[::-1][0:HOW_MANY_TO_PRINT]:
	print(str(count)+") "+probDict[i]+" ("+str(round(float(i)*100,3))+"%)")
	count+=1
