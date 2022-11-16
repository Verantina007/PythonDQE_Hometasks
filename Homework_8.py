import json  # import module for work with json
from Homework_7 import *  # import previous homeworks (5-6)


class ParseJSON:
    def input_post(self, post_text='', post_param=''):  # function for input data
        dict_with_posts = json.load(open('posts_to_add.json'))
        new_lines = []
        for i in range(0, len(dict_with_posts)):
            for key, value in dict_with_posts[i].items():
                new_lines.append(value)
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
                print(self.calculated_param, 'News added')
                new_lines = new_lines[i + 3:]
            elif 'privatad' in new_lines[i].lower():
                self.post_name = 'PrivatAd'
                self.post_text = new_lines[i + 1][:-1]
                self.post_param = new_lines[i + 2][:-1]
                self.calculated_param = PostPrivatAd().calculate_days(self.post_param)
                self.publish_post(self.calculated_param)
                print(self.calculated_param, 'Privatad added')
                new_lines = new_lines[i + 3:]
            elif 'weather forecast' in new_lines[i].lower():
                self.post_name = 'Weather Forecast'
                self.post_text = normalize_string(new_lines[i + 1])[:-2]
                self.post_param = normalize_string(new_lines[i + 2])[:-2]
                self.calculated_param = PostWeatherForecast().calculate_forecast(self.post_param)
                self.publish_post(self.calculated_param)
                print(self.calculated_param, 'Weather forecast added')
                new_lines = new_lines[i + 3:]

        os.remove('C:\\Users\\Vera_Varsotskaya\\PycharmProjects\\pythonProject4\\venv\\posts_to_add.json')

    def publish_post(self, calculated_param):  # publish for each type of posts
        PostStory().add_post(self.post_name, self.post_text, self.post_param, calculated_param)

def define_format(input_post_format=''):
    input_post_format = input(
        'Choose the input post format (1 - Text, 2 - File with posts, 3 - JSON file):\nNOTE:\nThe format for your .txt file is:\nType of post\nText of post\nInput parameter\nThe file should have .txt format and name \'posts_to_add.txt\'\nThe location of the file is:\nC:/Users/Vera_Varsotskaya/PycharmProjects/pythonProject4/venv\n\nNOTE:\nThe format for your .json file is:\n{"Type of post" : "Your type",\n"Text of post" : "your text of the post", \n"Input parameter" : "Your input parameter"}\nThe file should have .json format and name \'posts_to_add.json\'\nThe location of the file is:\nC:/Users/Vera_Varsotskaya/PycharmProjects/pythonProject4/venv\n\n')
    if input_post_format == '1':
        Publisher().input_post()
    elif input_post_format == '2':
        try:
            open('C:\\Users\\Vera_Varsotskaya\\PycharmProjects\\pythonProject4\\venv\\posts_to_add.txt', 'r')
        except FileNotFoundError:
            print('No such file or directory: "posts_to_add.txt"')
            exit()
        else:
            Publisher_file().input_post()
    elif input_post_format == '3':
        try:
            open('C:\\Users\\Vera_Varsotskaya\\PycharmProjects\\pythonProject4\\venv\\posts_to_add.json', 'r')
        except FileNotFoundError:
            print('No such file or directory: "posts_to_add.json"')
            exit()
        else:
            ParseJSON().input_post()
    else:
        print(
            "You've entered the wrong number! Choose the correct post format (1 - Text, 2 - File with one post, 3 - JSON file)")


define_format()
