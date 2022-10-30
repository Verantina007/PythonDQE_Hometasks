# #Homework_5
import datetime as dt
import time


class PostStory:  # create a class for writing posts in file
    def make_string(self, post_name, post_text, post_param,
                    calculated_param):  # function for creation of string, which will be published for each post
        self.string_for_post = f'{post_name}\n{post_text}\n{post_param}, {calculated_param}\n\n'

    def add_post(self, post_name, post_text, post_param, calculated_param):  # adding post in file
        self.make_string(post_name, post_text, post_param, calculated_param)
        file = open('posts.txt', 'a')
        file.write(f'{self.string_for_post}\n\n')
        file.close()


class PostNews(PostStory):  # child class for adding News
    def calculate_date(self):  # calculated parameter for News
        self.calculated_param = dt.datetime.now()
        return self.calculated_param


class PostPrivatAd(PostStory):  # child class for adding PrivatAd
    def calculate_days(self, post_param):  # calculated parameter for PrivatAd
        try:  # check the format of input date
            valid_date = time.strptime(post_param, '%d/%m/%Y')
        except ValueError:
            print('Invalid format of the date, it should be in format %d/%m/%Y')
            exit()
        self.calculated_param = (dt.datetime.strptime(post_param, "%d/%m/%Y") - dt.datetime.today()).days
        return self.calculated_param


class PostWeatherForecast(PostStory):  # child class for adding Weather forecast
    def calculate_forecast(self, post_param):
        if (post_param.startswith('+')) | (post_param.startswith('-')) | (
                post_param == '0'):  # check for format of weather degrees
            pass
        else:
            print('Invalid format of weather, it should be in format +/-2 or 0')
            exit()
        if post_param.startswith('+'):  # # calculated parameter for Weather forecast
            self.calculated_param = 'hot weather'
        elif post_param.startswith('-'):
            self.calculated_param = 'cold weather'
        elif post_param == '0':
            self.calculated_param = 'not hot or cold weather'
        return self.calculated_param


class Publisher:  # class for choosing type of post
    def input_post(self, post_text='', post_param='', ):  # function for input data
        self.number_of_the_post = input('Choose the type of your post (1 - News, 2 - Privat Ad, 3 - Weather forecast):')
        self.post_text = input('Enter the text of your post:')
        self.post_param = input('Enter the text of additional information:')
        if (self.post_text == '') | (self.post_param == ''):
            print("You've entered empty string in text of the post or in parameter")
            exit()
        if self.number_of_the_post == '1':
            self.post_name = 'News'
            self.calculated_param = PostNews().calculate_date()
        elif self.number_of_the_post == '2':
            self.post_name = 'PrivatAd'
            self.calculated_param = PostPrivatAd().calculate_days(self.post_param)
        elif self.number_of_the_post == '3':
            self.post_name = 'Weather Forecast'
            self.calculated_param = PostWeatherForecast().calculate_forecast(self.post_param)
        else:
            print(
                "You've entered the wrong number! Choose the correct type of your post (1 - News, 2 - Privat Ad, 3 - Weather forecast)")
            exit()
        self.publish_post(self.number_of_the_post, self.calculated_param)

    def publish_post(self, number_of_the_post, calculated_param):  # publish for each type of posts
        PostStory().add_post(self.post_name, self.post_text, self.post_param, calculated_param)


Publisher().input_post()
