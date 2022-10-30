# Homework 7

import csv #import module for work with csv
import os # import module for ability to delete files
from Homework_6 import * # import previous homeworks (5-6)

class CountWords:
    def parse_file(self, list_with_words):
        with open('posts.txt', 'r') as source_file: # open file with posts
            reader = csv.reader(source_file) # read each line of the file
            for row in reader:
                for element in row:
                    if element != []:
                        split_element = element.split(' ')
                        for word in split_element:
                            if word != '':
                                list_with_words.append(word.lower())
        return list_with_words

    def count_number(self, dict_for_words, list_with_words):
        for word in list_with_words:
            if word in dict_for_words.keys():
                dict_for_words[word]=dict_for_words[word]+1
            else:
                dict_for_words[word]=1
        return dict_for_words

    def write_words_csv(self, list_with_words=[], dict_for_words={}):
        if os.path.exists('C:\\Users\\Vera_Varsotskaya\\PycharmProjects\\pythonProject4\\venv\\words.csv'):
            os.remove(
                'C:\\Users\\Vera_Varsotskaya\\PycharmProjects\\pythonProject4\\venv\\words.csv')  # delete old file if exists
        if os.path.exists('C:\\Users\\Vera_Varsotskaya\\PycharmProjects\\pythonProject4\\venv\\letters.csv'):
            os.remove(
                'C:\\Users\\Vera_Varsotskaya\\PycharmProjects\\pythonProject4\\venv\\letters.csv')  # delete old file if exists
        self.parse_file(list_with_words)
        self.count_number(dict_for_words, list_with_words)
        with open('words.csv', 'w', newline='') as words_file: # open file with posts
            writer = csv.writer(words_file, delimiter='-', quotechar='"', quoting=csv.QUOTE_ALL) # read each line of the file
            for key in dict_for_words:
                writer.writerow([key, dict_for_words[key]])


# define_format() # to add new posts in posts.txt file
CountWords().write_words_csv()
