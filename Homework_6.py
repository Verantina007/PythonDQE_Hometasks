# Homework_6
import os
from Homework_5_v3 import *
from Homework_4 import normalize_string


class Publisher_file:  # class for choosing type of post
    def input_post(self, post_text='', post_param='', ):  # function for input data
        file = open('posts_to_add.txt', 'r')
        lines = file.readlines()
        file.close()
        for i in range(0, len(lines) - 1):
            lines[i] = normalize_string(lines[i])
            if lines[i] == '\n':
                i = i + 1
                pass
            elif lines[i] == 'News.\n':
                self.post_name = 'News'
                self.post_text = lines[i + 1][:-1]
                self.post_param = lines[i + 2][:-1]
                self.calculated_param = PostNews().calculate_date()
                self.publish_post(self.calculated_param)
                i = i + 3
            elif lines[i] == 'Privatad.\n':
                self.post_name = 'PrivatAd'
                self.post_text = lines[i + 1][:-1]
                self.post_param = lines[i + 2][:-1]
                self.calculated_param = PostPrivatAd().calculate_days(self.post_param)
                self.publish_post(self.calculated_param)
                i = i + 3
            elif lines[i] == 'Weather forecast.\n':
                self.post_name = 'Weather Forecast'
                self.post_text = lines[i + 1][:-1]
                self.post_param = lines[i + 2][:-1]
                self.calculated_param = PostWeatherForecast().calculate_forecast(self.post_param)
                self.publish_post(self.calculated_param)
                i = i + 3
        os.remove('C:\\Users\\Vera_Varsotskaya\\PycharmProjects\\pythonProject4\\venv\\posts_to_add.txt')

    def publish_post(self, calculated_param):  # publish for each type of posts
        PostStory().add_post(self.post_name, self.post_text, self.post_param, calculated_param)


def define_format(input_post_format=''):
    input_post_format = input(
        'Choose the input post format (1 - Text, 2 - File with posts):\nNOTE:\nThe format for your file is:\nType of post\nText of post\nInput parameter\nThe file should have txt format and name \'posts_to_add\'\nThe location of the file is:\nC:/Users/Vera_Varsotskaya/PycharmProjects/pythonProject4/venv\n')
    if input_post_format == '1':
        Publisher().input_post()
    elif input_post_format == '2':
        Publisher_file().input_post()
    else:
        print(
            "You've entered the wrong number! Choose the correct post format (1 - Text, 2 - File with one post)")


define_format()

# # imported function from Homework_4.py
# def normalize_string(str_for_normalization):  # function for normalization of the string
#     normalized_str = ''
#     for sentence in re.sub(r'\t', '', re.sub(r'\n', '', str_for_normalization)).lower().split('.'):
#         if re.search(r'\w', sentence):
#             sentence = sentence.strip().capitalize() + '.\n'
#             normalized_str += sentence
#     return normalized_str
