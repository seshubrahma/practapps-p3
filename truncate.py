import json
import pprint

f = open("truncated_train.json").read()
s = json.loads(f)



s['data'] = [s['data'][0]]
s['data'][0]['paragraphs'] = [s['data'][0]['paragraphs'][0]]
s['data'][0]['paragraphs'][0]['qas'] = [s['data'][0]['paragraphs'][0]['qas'][0]]


f = open("super_trun.json",'w')
f.write(json.dumps(s))
f.close()