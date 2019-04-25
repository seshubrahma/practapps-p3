import json
import uuid
import os

Dict = { }
#print("Initial nested dictionary:-")
#print(Dict)
squad_version = raw_input("What version of SQUAD are you using? ")
Dict['version'] = squad_version
count = 0;
article_name = ""
data_list = []
Dict['data'] = data_list
with open('nlp-qas.txt', "r") as read_file:
    for line in read_file:

        #add qas, id, etc in new_article_dict

        #new_article_dict['paragraphs']['qas']['question'] = line

                    
        if (count % 4 == 1):
            print ("mod is 1")
            new_article_dict['paragraphs']['qas']['id'] = uuid.uuid4().int
            new_article_dict['paragraphs']['qas']['question'] = line


        # article_name = raw_input("What is the name of the text file? Answer in no_01.txt format: ")
        if (count % 4 == 0):
            print ("mod is 0-getting article name")
            new_article_dict = {}
            new_article_dict['paragraphs'] = {}
            new_article_dict['paragraphs']['context'] = ""
            new_article_dict['paragraphs']['qas'] = {}
            new_article_dict['paragraphs']['qas']['answers'] = {}
            article_name = line
            new_article_dict['title'] = article_name
            #print (Dict)
        # new_article_dict['paragraphs']['qas'] = {}

        # impossible_answer = raw_input("Is your question possible to answer? Enter 'y' for yes and 'n' for no: ")
        # if impossible_answer == "n":
            #new_article_dict['paragraphs']['qas']['is_impossible'] = "true"
        # else:
            #new_article_dict['paragraphs']['qas']['is_impossible'] = "false"
            # new_article_dict['paragraphs']['qas']['answer_set'] = {}
        if (count % 4 == 2):
            print ("mod is 2")
            answer = line
            new_article_dict['paragraphs']['qas']['answers']['text'] = answer
            #print (Dict)
            if (answer == ""):
                new_article_dict['paragraphs']['qas']['is_impossible'] = "true"
            else:
                new_article_dict['paragraphs']['qas']['is_impossible'] = "false"
                #get index
                file_path = os.getcwd()
                #file_path = file_path[:-2]
                file_path += "/corefed_news/"
                file_path += article_name
                file_path_final  = file_path[:-1]
                answer = answer[:-1]
                with open(file_path_final, 'r') as f:
                    print ("opened the file")
                    print (file_path_final)
                    content = f.read()
                    index = content.find(answer)
                new_article_dict['paragraphs']['qas']['answers']['answer_start'] = index
            print ("leaving mod 2")
        
        if (count % 4 == 3):
            print ("mood is 3-getting context")
            new_article_dict['paragraphs']['context'] = line
            print (Dict) 
            data_list.append(new_article_dict)
            print (Dict)
            if (read_file.next() == "porterSwagOut"):
                break

        count += 1
        #create new entry for new line
       # data_list.append(new_article_dict)
    #new_entry = raw_input("would you like to add a new entry? Type 'y' to continue: ")



    with open('result2.json', 'w') as fp:
        json.dump(Dict, fp)
