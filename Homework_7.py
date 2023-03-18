# Homework 7

import csv  # import module for work with csv
import os  # import module for ability to delete files
from Homework_6 import *  # import previous homeworks (5-6)
# from parse_file_function import parse_file


class CountWords:
    @staticmethod
    def parse_file(path_file='C:\\Users\\Vera_Varsotskaya\\PycharmProjects\\pythonProject4\\venv\\posts.txt'):
        with open(path_file, 'r') as source_file:  # open file with posts
            reader = csv.reader(source_file)  # read each line of the file
            list_with_words =  []
            for row in reader:
                for element in row:
                    if element != []:
                        split_element = element.split(' ')
                        for word in split_element:
                            if word != '':
                                list_with_words.append(word.lower())
        return list_with_words

    def count_number(self, list_with_words):
        dict_for_words = {}
        for word in list_with_words:
            if word in dict_for_words.keys():
                dict_for_words[word] = dict_for_words[word] + 1
            else:
                dict_for_words[word] = 1
        return dict_for_words

    def write_words_csv(self, path_words='C:\\Users\\Vera_Varsotskaya\\PycharmProjects\\pythonProject4\\venv\\words.csv'):
        if os.path.exists(path_words):
            os.remove(path_words)  # delete old file if exists
        list_with_words = self.parse_file()
        dict_for_words=self.count_number(list_with_words)
        with open('words.csv', 'w', newline='') as words_file:  # open file with posts
            writer = csv.writer(words_file, delimiter='-', quotechar='"',
                                quoting=csv.QUOTE_ALL)  # read each line of the file
            for key in dict_for_words:
                writer.writerow([key, dict_for_words[key]])


class CountLetters:
    @staticmethod
    def parse_file(path_file='C:\\Users\\Vera_Varsotskaya\\PycharmProjects\\pythonProject4\\venv\\posts.txt'):
        with open(path_file, 'r') as source_file:  # open file with posts
            reader = csv.reader(source_file)  # read each line of the file
            string_with_letters=''
            for row in reader:
                for element in row:
                    for char in element:
                        if char.isalpha():
                            string_with_letters = string_with_letters + char
        return string_with_letters

    def count_values(self, string_with_letters):
        number_of_all_letters = len(string_with_letters)
        dict_with_letters={}
        for letter in string_with_letters:
            if letter.lower() in dict_with_letters.keys():
                number_of_letter = dict_with_letters[letter.lower()][0] + 1
                if letter.isupper():
                    number_of_uppercase = dict_with_letters[letter.lower()][1] + 1
                else:
                    number_of_uppercase = dict_with_letters[letter.lower()][1]
                persent_letter = (dict_with_letters[letter.lower()][0] / number_of_all_letters) * 100
                dict_with_letters[letter.lower()] = [number_of_letter, number_of_uppercase, persent_letter]
            if letter.lower() not in dict_with_letters.keys():
                number_of_letter = 1
                if letter.isupper():
                    number_of_uppercase = 1
                else:
                    number_of_uppercase = 0
                persent_letter = (number_of_letter / number_of_all_letters) * 100
                dict_with_letters[letter.lower()] = [number_of_letter, number_of_uppercase, persent_letter]
        return dict_with_letters

    def write_letters_csv(self, path_letters='C:\\Users\\Vera_Varsotskaya\\PycharmProjects\\pythonProject4\\venv\\letters.csv'):
        if os.path.exists(path_letters):
            os.remove(path_letters)  # delete old file if exists
        string_with_letters = self.parse_file()
        dict_with_letters = self.count_values(string_with_letters)
        with open('letters.csv', 'w', newline='') as letters_file:  # open file with posts
            headers = ['letter in lower case', 'number of letters in any case', 'number of letter in uppercase',
                       '% of letter in all letters']
            writer = csv.DictWriter(letters_file, fieldnames=headers, delimiter=',', quotechar='"',
                                    quoting=csv.QUOTE_ALL)  # read each line of the file
            writer.writeheader()
            for key in dict_with_letters:
                writer.writerow(
                    {'letter in lower case': key, 'number of letters in any case': dict_with_letters[key][0],
                     'number of letter in uppercase': dict_with_letters[key][1],
                     '% of letter in all letters': f'{dict_with_letters[key][2]:.2f}%'})


if __name__ == '__main__':
    CountWords().write_words_csv()
    CountLetters().write_letters_csv()
