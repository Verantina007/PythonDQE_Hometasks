# #Homework_5
import datetime as dt

# define class for work with News
class News:
    def __init__(self, name_of_post='News', text='', city='', date=''):
        self.name_of_post = name_of_post
        self.text = input('Enter the text of the News:')
        self.city = input('Enter the name of the city:')
        self.date = dt.datetime.now()

    def publish(self):
        file = open('posts.txt', 'a')
        file.write(self.name_of_post+'\n'+self.text+'\n'+self.city+', '+str(self.date)+'\n\n')
        file.close()


class PrivatAd:
    def __init__(self, name_of_post='Privat Ad', text='', expiration_date='', number_of_days=''):
        self.name_of_post = name_of_post
        self.text = input('Enter the text of the Privat Ad:')
        self.expiration_date = input('Enter the experation date of your Privat Ad in format DD/MM/YYYY:')
        self.number_of_days = (dt.datetime.strptime(self.expiration_date, "%d/%m/%Y") - dt.datetime.today()).days

    def publish(self):
        file = open('posts.txt', 'a')
        file.write(self.name_of_post+'\n'+self.text+'\nActual until: '+self.expiration_date+', '+str(self.number_of_days)+' days\n\n')
        file.close()

class WeatherForecast:
    def __init__(self, name_of_post='Weather forecast', degrees=''):
        self.name_of_post = name_of_post
        self.degrees = input('Enter the weather forecast for a day in format +/-20.2 C')
        self.result = self.weather_condition()

    def weather_condition(self):
        if self.degrees.startswith('+'):
            self.result = 'hot weather'
        elif self.degrees.startswith('-'):
            self.result = 'cold weather'
        elif self.degrees == '0 C':
            self.result = 'not hot or cold'
        return self.result

    def publish(self):
        file = open('posts.txt', 'a')
        file.write(self.name_of_post+'\nThe weather forecast for today is: '+self.degrees+'\nWe are having '+self.result+'\n\n')
        file.close()


class ChoseYourPost:
    def __init__(self, number_of_the_post=''):
        self.number_of_the_post = input('Choose the type of your post (1 - News, 2 - Privat Ad, 3 - Weather forecast):')

    def publish_post(self, number_of_the_post=''):
        if self.number_of_the_post == '1':
            News().publish()
        elif self.number_of_the_post == '2':
            PrivatAd().publish()
        elif self.number_of_the_post == '3':
            WeatherForecast().publish()
        else:
            print ("You've entered the wrong number!")


ChoseYourPost().publish_post()

