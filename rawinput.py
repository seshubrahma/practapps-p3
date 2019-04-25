import json
import uuid
import os

Dict = { }
squad_version = raw_input("What version of SQUAD are you using? ")
Dict['version'] = squad_version
count = 0;
article_name = ""
data_list = []
Dict['data'] = data_list
with open('nlp-qas.txt', "r") as read_file:
    for line in read_file:
                    
        if (count % 4 == 1):
            new_article_dict['paragraphs']['qas']['id'] = uuid.uuid4().int
            new_article_dict['paragraphs']['qas']['question'] = line

        if (count % 4 == 0):
            new_article_dict = {}
            new_article_dict['paragraphs'] = {}
            new_article_dict['paragraphs']['context'] = ""
            new_article_dict['paragraphs']['qas'] = {}
            new_article_dict['paragraphs']['qas']['answers'] = {}
            article_name = line
            new_article_dict['title'] = article_name

        if (count % 4 == 2):
            answer = line
            new_article_dict['paragraphs']['qas']['answers']['text'] = answer
            if (answer == ""):
                new_article_dict['paragraphs']['qas']['is_impossible'] = "true"
            else:
                new_article_dict['paragraphs']['qas']['is_impossible'] = "false"
                #get index
                file_path = os.getcwd()
                file_path += "/corefed_news/"
                file_path += article_name
                file_path_final  = file_path[:-1]
                answer = answer[:-1]
                with open(file_path_final, 'r') as f:
                    content = f.read()
                    index = content.find(answer)
                new_article_dict['paragraphs']['qas']['answers']['answer_start'] = index
        
        if (count % 4 == 3):
            new_article_dict['paragraphs']['context'] = line
            data_list.append(new_article_dict)
            if (read_file.next() == "porterSwagOut"):
                break

        count += 1

    with open('groundtruth.json', 'w') as fp:
        json.dump(Dict, fp)
