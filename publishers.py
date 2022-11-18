import os
import json
import xml.etree.ElementTree as ET
from additional_classes import *
from additional_functions import *


class PublisherInputText:  # class for choosing type of post
    def input_post(self, post_text='', post_param=''):  # function for input data
        self.number_of_the_post = input('Choose the type of your post (1 - News, 2 - Privat Ad, 3 - Weather forecast):')
        if (self.number_of_the_post != '1') & (self.number_of_the_post != '2') & (self.number_of_the_post != '3'):
            print(
                "You've entered the wrong number! Choose the correct type of your post (1 - News, 2 - Privat Ad, 3 - Weather forecast)")
            exit()
        self.post_text = input('Enter the text of your post:')
        self.post_param = input('Enter the text of additional information:')
        if self.number_of_the_post == '1':
            self.post_name = 'News'
            self.calculated_param = PostNews().calculate_date()
            write_news_database(self.post_text, self.post_param, self.calculated_param)
        elif self.number_of_the_post == '2':
            self.post_name = 'PrivatAd'
            self.calculated_param = PostPrivatAd().calculate_days(self.post_param)
            write_privatads_database(self.post_text, self.post_param, self.calculated_param)
        elif self.number_of_the_post == '3':
            self.post_name = 'Weather Forecast'
            self.calculated_param = PostWeatherForecast().calculate_forecast(self.post_param)
            write_weather_database(self.post_text, self.post_param, self.calculated_param)
        self.publish_post(self.number_of_the_post, self.calculated_param)

    def publish_post(self, number_of_the_post, calculated_param):  # publish for each type of posts
        PostStory().add_post(self.post_name, self.post_text, self.post_param, calculated_param)


class PublisherTXTFile:  # class for choosing type of post
    def input_post(self, post_text='', post_param='', path='C:\\Users\\Vera_Varsotskaya\\PycharmProjects\\pythonProject5\\'):  # function for input data
        file = open(path+'posts_to_add.txt', 'r')
        lines = file.readlines()
        file.close()
        new_lines = []
        for i in range(0, len(lines)):
            if (lines[i] != '') & (lines[i] != '\n'):
                new_lines.append(lines[i])
        print(new_lines)

        i = 0
        while len(new_lines) >= 3:
            i = 0
            if 'news' in new_lines[i].lower():
                self.post_name = 'News'
                self.post_text = new_lines[i + 1][:-1]
                self.post_param = new_lines[i + 2][:-1]
                self.calculated_param = PostNews().calculate_date()
                self.publish_post(self.calculated_param)
                write_news_database(self.post_text, self.post_param, self.calculated_param)
                print('News added')
                new_lines = new_lines[i + 3:]
            elif 'privatad' in new_lines[i].lower():
                self.post_name = 'PrivatAd'
                self.post_text = new_lines[i + 1][:-1]
                self.post_param = new_lines[i + 2][:-1]
                self.calculated_param = PostPrivatAd().calculate_days(self.post_param)
                self.publish_post(self.calculated_param)
                write_privatads_database(self.post_text, self.post_param, self.calculated_param)
                print('Privatad added')
                new_lines = new_lines[i + 3:]
            elif 'weather forecast' in new_lines[i].lower():
                self.post_name = 'Weather Forecast'
                self.post_text = normalize_string(new_lines[i + 1])[:-2]
                self.post_param = normalize_string(new_lines[i + 2])[:-2]
                self.calculated_param = PostWeatherForecast().calculate_forecast(self.post_param)
                self.publish_post(self.calculated_param)
                write_weather_database(self.post_text, self.post_param, self.calculated_param)
                print('Weather forecast added')
                new_lines = new_lines[i + 3:]

        os.remove(path+'posts_to_add.txt')

    def publish_post(self, calculated_param):  # publish for each type of posts
        PostStory().add_post(self.post_name, self.post_text, self.post_param, calculated_param)


class PublisherJSONFile:
    def input_post(self, post_text='', post_param='', path='C:\\Users\\Vera_Varsotskaya\\PycharmProjects\\pythonProject5\\'):  # function for input data
        dict_with_posts = json.load(open(path+'posts_to_add.json'))
        new_lines = []
        for i in range(0, len(dict_with_posts)):
            for key, value in dict_with_posts[i].items():
                new_lines.append(value)

        i = 0
        while len(new_lines) >= 3:
            i = 0
            if 'news' in new_lines[i].lower():
                self.post_name = 'News'
                self.post_text = new_lines[i + 1][:-1]
                self.post_param = new_lines[i + 2][:-1]
                self.calculated_param = PostNews().calculate_date()
                self.publish_post(self.calculated_param)
                write_news_database(self.post_text, self.post_param, self.calculated_param)
                print(self.calculated_param, 'News added')
                new_lines = new_lines[i + 3:]
            elif 'privatad' in new_lines[i].lower():
                self.post_name = 'PrivatAd'
                self.post_text = new_lines[i + 1][:-1]
                self.post_param = new_lines[i + 2][:]
                self.calculated_param = PostPrivatAd().calculate_days(self.post_param)
                self.publish_post(self.calculated_param)
                write_privatads_database(self.post_text, self.post_param, self.calculated_param)
                print(self.calculated_param, 'Privatad added')
                new_lines = new_lines[i + 3:]
            elif 'weather forecast' in new_lines[i].lower():
                self.post_name = 'Weather Forecast'
                self.post_text = normalize_string(new_lines[i + 1])[:-2]
                self.post_param = normalize_string(new_lines[i + 2])[:-2]
                self.calculated_param = PostWeatherForecast().calculate_forecast(self.post_param)
                self.publish_post(self.calculated_param)
                write_weather_database(self.post_text, self.post_param, self.calculated_param)
                print(self.calculated_param, 'Weather forecast added')
                new_lines = new_lines[i + 3:]

        os.remove(path+'posts_to_add.json')

    def publish_post(self, calculated_param):  # publish for each type of posts
        PostStory().add_post(self.post_name, self.post_text, self.post_param, calculated_param)


class PublisherXMLFile:
    def input_post(self, post_text='', post_param='', path='C:\\Users\\Vera_Varsotskaya\\PycharmProjects\\pythonProject5\\'):  # function for input data
        try:
            ET.parse(path + 'posts_to_add.xml')
        except ET.ParseError:
            print('Your .xml file is incorrect')
            exit()

        xml_file = ET.parse(path+'posts_to_add.xml')
        root=xml_file.getroot()
        for post in root.iter():
            if post.get('name') == 'News':
                self.post_name = 'News'
                for child in post:
                    if child.tag == 'text_of_post':
                        self.post_text = child.text
                    if child.tag == 'input_parameter':
                        self.post_param = child.text
                self.calculated_param = PostNews().calculate_date()
                self.publish_post(self.calculated_param)
                write_news_database(self.post_text, self.post_param, str(self.calculated_param))
                print(self.calculated_param, 'News added')
            if post.get('name') == 'PrivatAd':
                self.post_name = 'PrivatAd'
                for child in post:
                    if child.tag == 'text_of_post':
                        self.post_text = child.text
                    if child.tag == 'input_parameter':
                        self.post_param = child.text
                self.calculated_param = PostPrivatAd().calculate_days(self.post_param)
                self.publish_post(self.calculated_param)
                write_privatads_database(self.post_text, self.post_param, self.calculated_param)
                print(self.calculated_param, 'Privatad added')
            if post.get('name') == 'Weather Forecast':
                self.post_name = 'Weather Forecast'
                for child in post:
                    if child.tag == 'text_of_post':
                        self.post_text = child.text
                    if child.tag == 'input_parameter':
                        self.post_param = child.text
                self.calculated_param = PostWeatherForecast().calculate_forecast(self.post_param)
                self.publish_post(self.calculated_param)
                write_weather_database(self.post_text, self.post_param, self.calculated_param)
                print(self.calculated_param, 'Weather forecast added')

        os.remove(path+'posts_to_add.xml')

    def publish_post(self, calculated_param):  # publish for each type of posts
        PostStory().add_post(self.post_name, self.post_text, self.post_param, calculated_param)


