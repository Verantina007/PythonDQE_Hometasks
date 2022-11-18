import re  # library for useing regex
import pyodbc

def normalize_string(str_for_normalization):  # function for normalization of the string
    normalized_str = ''
    for sentence in re.sub(r'\t', '', re.sub(r'\n', '', str_for_normalization)).lower().split('.'):
        if re.search(r'\w', sentence):
            sentence = sentence.strip().capitalize() + '.\n'
            normalized_str += sentence
    return normalized_str


def write_news_database (post_text, post_param, calculated_param, conn_string='Driver={SQL Server};Server=EPBYMINW0E8A\\SQLEXPRESS;DATABASE=testdatabase;Trusted_Connection=yes'):
    connection = pyodbc.connect(conn_string)
    cursor = connection.cursor()
    cursor.execute('''IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='news' and xtype='U')
            CREATE TABLE news (post_text varchar (200), additional_parameter varchar(20), calculated_parameter varchar(30))''')
    connection.commit()
    cursor.execute('SELECT * FROM news')
    result = cursor.fetchall()
    i=0
    for element in result:
        if (element[0] == post_text) & (element[1] == post_param) & (element[2] == calculated_param):
            i=i+1
    if i==0:
        cursor.execute("INSERT INTO news VALUES ('%(post_text)s', '%(post_param)s', '%(calculated_param)s')" % {'post_text': post_text, 'post_param': post_param, 'calculated_param': calculated_param})
        connection.commit()
    cursor.close()
    connection.close()


def write_privatads_database (post_text, post_param, calculated_param, conn_string='Driver={SQL Server};Server=EPBYMINW0E8A\\SQLEXPRESS;DATABASE=testdatabase;Trusted_Connection=yes'):
    connection = pyodbc.connect(conn_string)
    cursor = connection.cursor()
    cursor.execute('''IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='privatads' and xtype='U')
        CREATE TABLE privatads (post_text varchar (200), additional_parameter varchar(20), calculated_parameter integer)''')
    connection.commit()
    cursor.execute('SELECT * FROM privatads')
    result = cursor.fetchall()
    i=0
    for element in result:
        if (element[0] == post_text) & (element[1] == post_param) & (element[2] == calculated_param):
            i=i+1
    if i==0:
        cursor.execute("INSERT INTO privatads VALUES ('%(post_text)s', '%(post_param)s', '%(calculated_param)s')" % {'post_text': post_text, 'post_param': post_param, 'calculated_param': calculated_param})
        connection.commit()
    cursor.close()
    connection.close()


def write_weather_database (post_text, post_param, calculated_param, conn_string='Driver={SQL Server};Server=EPBYMINW0E8A\\SQLEXPRESS;DATABASE=testdatabase;Trusted_Connection=yes'):
    connection = pyodbc.connect(conn_string)
    cursor = connection.cursor()
    cursor.execute('''IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='weatherforecast' and xtype='U')
        CREATE TABLE weatherforecast (post_text varchar (200), additional_parameter varchar(20), calculated_parameter varchar(20))''')
    connection.commit()
    cursor.execute('SELECT * FROM weatherforecast')
    result = cursor.fetchall()
    i = 0
    for element in result:
        if (element[0] == post_text) & (element[1] == post_param) & (element[2] == calculated_param):
            i = i + 1
    if i == 0:
        cursor.execute("INSERT INTO weatherforecast VALUES ('%(post_text)s', '%(post_param)s', '%(calculated_param)s')" % {'post_text': post_text, 'post_param': post_param, 'calculated_param': calculated_param})
        connection.commit()
    cursor.close()
    connection.close()
