from __future__ import print_function
from collections import Counter
import string
import re
import argparse
import json
import sys
import Levenshtein


def f1_score(prediction, ground_truth):
    prediction_tokens = prediction.split()
    ground_truth_tokens = ground_truth.split()
    common = Counter(prediction_tokens) & Counter(ground_truth_tokens)
    num_same = sum(common.values())
    if num_same == 0:
        num_same = 1.0
    precision = 1.0 * num_same / (len(prediction_tokens) + 1)
    recall = 1.0 * num_same / (len(ground_truth_tokens) + 1)
    f1 = (2 * precision * recall) / (precision + recall)
    return f1


def exact_match_score(prediction, ground_truth):
    return (1 / (Levenshtein.distance(prediction, ground_truth) + 1))


def metric_max_over_ground_truths(metric_fn, prediction, ground_truths):
    scores_for_ground_truths = []
    for ground_truth in ground_truths:
        score = metric_fn(prediction, ground_truth)
        scores_for_ground_truths.append(score)
    return max(scores_for_ground_truths)


def evaluate(dataset, predictions):
    f1 = exact_match = total = 0

    for article in dataset:
        for paragraph in article['paragraphs']:
            for qa in paragraph['qas']:
                total += 1
                # if qa['id'] not in predictions:
                #     print('Unanswered question ' + qa['id'] + ' will receive score 0.')
                #     continue
                ground_truths = list(map(lambda x: x['text'], qa['answers'])) #list that has all the ground truth answers 

                #if anything in predictions matches anything in the ground_truths list
                most_similar_ratio = 0
                for uuid in predictions:
                    for answer in range(len(predictions[uuid])):
                        current_ratio = Levenshtein.ratio(ground_truths[0], predictions[uuid][answer]['text'])
                        if current_ratio > most_similar_ratio:
                            most_similar_ratio = current_ratio
                            most_similar_prediction = predictions[uuid][answer]['text']

                # qa_id = qa['id'].encode('ascii','ignore')
                prediction = most_similar_prediction
                exact_match += metric_max_over_ground_truths(exact_match_score, prediction, ground_truths)
                f1 += metric_max_over_ground_truths(f1_score, prediction, ground_truths)

    exact_match = 100.0 * exact_match / total
    f1 = 100.0 * f1 / total

    return {'exact_match': exact_match, 'f1': f1}


if __name__ == '__main__':
    expected_version = '2.0'
    parser = argparse.ArgumentParser(description='Evaluation for SQuAD ' + expected_version)
    parser.add_argument('dataset_file', help='Dataset file')
    parser.add_argument('prediction_file', help='Prediction File')
    args = parser.parse_args()
    
    with open(args.dataset_file) as dataset_file:
        dataset_json = json.load(dataset_file)
        dataset = dataset_json['data']
    
    with open(args.prediction_file) as prediction_file:
        predictions = json.load(prediction_file)
    
    print(json.dumps(evaluate(dataset, predictions)))
