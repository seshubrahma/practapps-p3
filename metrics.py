import json

def main()

	expected_set = set() #fill this with the question answer pairs we created
	add_expected_ground_truth(expected_set)




	actual_set = set() #fill this with what squad outputs (json)
	add_actual_output(actual_set)



def add_expected_ground_truth(expected_set):
	#read from text file?
	#set of tuples (q,a)


def add_actual_output(actual_set):
	#parse json

	with open('.json', 'r') as f:
	output = json.load(f)


def calculate_metrics(actual, expected, name):
    correct = actual.intersection(expected) #actual == type(set)
    precision = len(correct) / len(actual)
    recall = len(correct) / len(expected)

    print(name)
    print(f'Precision: {precision}')
    print(f'Recall: {recall}')


if __name__ == '__main__':
	main()
