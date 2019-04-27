import spacy
import os
#if we want to use nltk
#import nltk.data

#go into corefed_news folder

#for each file
#made a article(num)paragraph.txt
#use spacy .sents to get each sentence in a text file
#counter int
#put first four sentences in paragraph.txt
#multiple text files with one paragraph each FOR one news article txt

def main(text, filename):
    output_dir = 'orig_news_paragraphs'
    make_paragraphs(text, filename, output_dir)


def make_paragraphs(text, filename, output_dir):

    #if we want to use nltk
    # sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    # print(sent_detector.tokenize(text.strip()))



    doc = nlp(text)
    all_sentences = [sent for sent in doc.sents]
    
    counter = 0
    index = 0
    paragraph_counter = 0
    output_filename = filename[:-4]+'_p'+str(paragraph_counter)+'.txt'
    output_file = os.path.join(output_dir, output_filename)
    
    while (index != len(all_sentences)-1):
        if counter == 4:
            counter = 0
            index -= 1
            paragraph_counter += 1
            output_filename = filename[:-4]+'_p'+str(paragraph_counter)+'.txt'
            output_file = os.path.join(output_dir, output_filename)

            print(output_filename)

        with open(output_file, 'w', encoding='utf8') as f:
            while ((counter < 4) and (index != len(all_sentences)-1)):
                f.write(str(all_sentences[index]) +" ")
                counter += 1
                index += 1



if __name__ == '__main__':
    nlp = spacy.load('en')
    
    directory_name = 'orig_news'
    directory = os.fsencode(directory_name)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        
        if filename.endswith('.txt'):
        # if filename == 'no_1.txt':
            input_file = os.path.join(directory_name, filename)
            print("input_file", input_file)
            with open(input_file) as f:
                text = f.read()
                main(text, filename)

