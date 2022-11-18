from publishers import *

def define_format(path='C:\\Users\\Vera_Varsotskaya\\PycharmProjects\\pythonProject5\\'):
    input_post_format = input(
        'Choose the input post format (1 - Text, 2 - File with posts, 3 - JSON file, 4 - XML file):\nNOTE:\nThe format for your .txt file is:\nType of post\nText of post\nInput parameter\nThe file should have .txt format and name \'posts_to_add.txt\'\nThe location of the file is:\nC:/Users/Vera_Varsotskaya/PycharmProjects/pythonProject5\n\nNOTE:\nThe format for your .json file is:\n{"Type of post" : "Your type",\n"Text of post" : "your text of the post", \n"Input parameter" : "Your input parameter"}\nThe file should have .json format and name \'posts_to_add.json\'\nThe location of the file is:\nC:/Users/Vera_Varsotskaya/PycharmProjects/pythonProject5\n\nNOTE:\nThe format for your .xml file is:\n<posts_to_add>\n<post name="Your type of post">\n<text_of_post>"your text of the post"</text_of_post>\n<input_parameter>"Your input parameter"</input_parameter>\n</post>\nThe file should have .xml format and name \'posts_to_add.xml\'\nThe location of the file is:\nC:/Users/Vera_Varsotskaya/PycharmProjects/pythonProject5\n\n')
    if input_post_format == '1':
        PublisherInputText().input_post()
    elif input_post_format == '2':
        try:
            open(path+'posts_to_add.txt', 'r')
        except FileNotFoundError:
            print(f'No such file or directory: "posts_to_add.txt" in the {path}')
            exit()
        else:
            PublisherTXTFile().input_post()
    elif input_post_format == '3':
        try:
            open(path+'posts_to_add.json', 'r')
        except FileNotFoundError:
            print(f'No such file or directory: "posts_to_add.json" in the {path}')
            exit()
        else:
            PublisherJSONFile().input_post()
    elif input_post_format == '4':
        print(4)
        try:
            open(path+'posts_to_add.xml', 'r')
        except FileNotFoundError:
            print(f'No such file or directory: "posts_to_add.xml"in th {path}')
            exit()
        else:
            PublisherXMLFile().input_post()
    else:
        print(
            "You've entered the wrong number! Choose the correct post format (1 - Text, 2 - File with one post, 3 - JSON file, 4 - XML file)")

define_format()

CountWords().write_words_csv()
CountLetters().write_letters_csv()
