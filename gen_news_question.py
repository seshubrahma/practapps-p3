import uuid
import copy
import os
import json
import pprint
import spacy

questionWeAreAsking = 'When was Donald J. Trump born?'

nlp = spacy.load("en_core_web_sm")
doc = nlp(questionWeAreAsking)

named_ents = []
for ent in doc.noun_chunks:
	named_ents.append(ent.text.lower().replace("the","").strip())

for rem in ['who','what','where','when','which','how']:
	try:
		named_ents.remove(rem)
	except:
		pass

print(named_ents)

f = open("truncated_train.json").read()
s = json.loads(f)

paragraphs = []
for file in os.listdir('orig_news_paragraphs'):
	paragraphs.append(open('orig_news_paragraphs/'+file).read())

s['data'] = [s['data'][0]]
s['data'][0]['paragraphs'] = [s['data'][0]['paragraphs'][0]]
s['data'][0]['paragraphs'][0]['qas'] = [s['data'][0]['paragraphs'][0]['qas'][0]]
testObj = copy.deepcopy(s['data'][0]['paragraphs'][0]['qas'][0])
del s['data'][0]['paragraphs'][0]

for p in paragraphs:
	p = p.lower()
	doingParagraph = False
	for ne in named_ents:
		if ne in p:
			doingParagraph = True
	if doingParagraph:
		print(p)
		qObj = copy.deepcopy(testObj)
		qObj['question'] = questionWeAreAsking
		qObj['id'] = str(uuid.uuid4())
		pobj = {}
		pobj['context'] = p
		pobj['qas'] = [qObj]
		s['data'][0]['paragraphs'].append(pobj)

f = open("newsQuestions.json",'w')
f.write(json.dumps(s))
f.close()