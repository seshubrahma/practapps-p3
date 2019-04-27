import json
import uuid
import os

big_dict = {}
squad_version = raw_input("What version of SQUAD are you using? ")
big_dict['version'] = squad_version
count = 0;
article_name = ""
data_list = []
big_dict['data'] = data_list

with open('nlp-qas.txt', "r") as read_file:
    for line in read_file:

        if (count % 4 == 0):
            new_article_dict = {}

            paragraph_list = []
            new_article_dict['paragraphs'] = paragraph_list
            paragraph_dict = {}
            paragraph_list.append(paragraph_dict)
            paragraph_dict['context'] = ""

            qas_list = []
            paragraph_dict['qas'] = qas_list
            qas_dict = {}
            qas_list.append(qas_dict)

            answers_list = []
            qas_dict['answers'] = answers_list
            answers_dict = {}
            answers_list.append(answers_dict)
            answers_dict['answer_start'] = 0
            answers_dict['text'] = ""
            qas_dict['question'] = ""
            qas_dict['id'] = ""
            qas_dict['is_impossible'] = ""
            
            article_name = line
            new_article_dict['title'] = article_name[:-1]


        if (count % 4 == 1):
            new_article_dict['paragraphs'][0]['qas'][0]['id'] = str(uuid.uuid4().int)
            new_article_dict['paragraphs'][0]['qas'][0]['question'] = line[:-1]


        if (count % 4 == 2):
            answer = line
            new_article_dict['paragraphs'][0]['qas'][0]['answers'][0]['text'] = answer[:-1]

            if (answer == "\n"):
                new_article_dict['paragraphs'][0]['qas'][0]['is_impossible'] = "true"
            else:
                new_article_dict['paragraphs'][0]['qas'][0]['is_impossible'] = "false"
                #get index
                file_path = os.getcwd()
                file_path += "/corefed_news/"
                file_path += article_name
                file_path_final  = file_path[:-1]
                answer = answer[:-1]
                with open(file_path_final, 'r') as f:
                    content = f.read()
                    index = content.find(answer)
                new_article_dict['paragraphs'][0]['qas'][0]['answers'][0]['answer_start'] = index
        
        if (count % 4 == 3):
            new_article_dict['paragraphs'][0]['context'] = line[:-1]
            
            data_list.append(new_article_dict)
            if (read_file.next() == "porterSwagOut"):
                break

        count += 1

    with open('groundtruth.json', 'w') as fp:
        json.dump(big_dict, fp)
