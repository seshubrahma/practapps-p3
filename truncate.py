import uuid
import copy
import os
import json
import pprint

questionWeAreAsking = 'Who is president of the United States?'

f = open("truncated_train.json").read()
s = json.loads(f)

paragraphs = []
for file in os.listdir('corefed_news')[:10]:
	paragraphs.append(open('corefed_news/'+file).read())

print paragraphs

s['data'] = [s['data'][0]]
s['data'][0]['paragraphs'] = [s['data'][0]['paragraphs'][0]]
s['data'][0]['paragraphs'][0]['qas'] = [s['data'][0]['paragraphs'][0]['qas'][0]]
testObj = copy.deepcopy(s['data'][0]['paragraphs'][0]['qas'][0])
del s['data'][0]['paragraphs'][0]

for p in paragraphs:
	qObj = copy.deepcopy(testObj)
	qObj['question'] = questionWeAreAsking
	qObj['id'] = str(uuid.uuid4())
	pobj = {}
	pobj['context'] = p
	pobj['qas'] = [qObj]
	s['data'][0]['paragraphs'].append(pobj)

s['data'][0]['paragraphs']

f = open("newsQuestions.json",'w')
f.write(json.dumps(s))
f.close()