# #Homework_5
import datetime as dt
import time


class PostStory:
    def __init__(self, post_name, post_text, post_param, calculated_parem='', string_for_post=''):
        self.post_name = post_name
        self.post_text = post_text
        self.post_param = post_param
        self.calculated_parem = calculated_parem
        self.string_for_post = string_for_post

    def make_string(self):
        self.string_for_post=f'{self.post_name}\n{self.post_text}\n{self.post_param}, {self.calculated_parem}\n\n'

    def add_post (self):
        self.make_string()
        file = open('posts.txt', 'a')
        file.write(f'{self.string_for_post}\n\n')
        file.close()
#        print(f'{self.string_for_post}')


class PostNews(PostStory):
    def calculate_date(self):
        self.calculated_parem = dt.datetime.now()

    def post_news(self):
        self.calculate_date()
        self.add_post()
#        print(f'{self.string_for_post}')


class PostPrivatAd(PostStory):
    def calculate_days(self):
        try:
            valid_date = time.strptime(self.post_param, '%d/%m/%Y')
        except ValueError:
            print('Invalid format of the date, it should be in format %d/%m/%Y')
            exit()
        self.calculated_parem = (dt.datetime.strptime(self.post_param, "%d/%m/%Y") - dt.datetime.today()).days

    def post_privatad(self):
        self.calculate_days()
        self.add_post()
#        print(f'{self.string_for_post}')


class PostWeatherForecast(PostStory):
    def calculate_forecast(self):
        try:
            if (self.post_param.startswith('+')) | (self.post_param.startswith('-')) | (self.post_param == '0'):
                pass
            else:
                raise Exception ('Invalid format of weather, it should be in format +/-2')
        except Exception as error:
            print(error)
            exit()
        if self.post_param.startswith('+'):
            self.calculated_parem = 'hot weather'
        elif self.post_param.startswith('-'):
            self.calculated_parem = 'cold weather'
        elif self.post_param == '0 C':
            self.calculated_parem = 'not hot or cold'

    def post_forecast(self):
        self.calculate_forecast()
        self.add_post()
#        print(f'{self.string_for_post}')


class ChoseYourPost:
    def __init__(self, number_of_the_post=''):
        self.number_of_the_post = input('Choose the type of your post (1 - News, 2 - Privat Ad, 3 - Weather forecast):')

    def input_post(self, post_text='', post_param='',):
        self.post_text = input('Enter the text of your post:')
        self.post_param = input('Enter the text of additional information:')
        try:
            if (self.post_text == '') | (self.post_param == '') :
                raise Exception ("You've entered empty string in text of the post or in parametr")
            else:
                pass
        except Exception as error:
            print(error)
            exit()

    def publish_post(self, number_of_the_post=''):
        if self.number_of_the_post == '1':
            self.post_name='News'
            self.input_post()
            PostNews(self.post_name, self.post_text, self.post_param).post_news()
        elif self.number_of_the_post == '2':
            self.post_name = 'PrivatAd'
            self.input_post()
            PostPrivatAd(self.post_name, self.post_text, self.post_param).post_privatad()
        elif self.number_of_the_post == '3':
            self.post_name = 'Weather Forecast'
            self.input_post()
            PostWeatherForecast(self.post_name, self.post_text, self.post_param).post_forecast()
        else:
            print ("You've entered the wrong number! Choose the correct type of your post (1 - News, 2 - Privat Ad, 3 - Weather forecast)")


ChoseYourPost().publish_post()
