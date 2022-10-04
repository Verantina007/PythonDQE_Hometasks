# Homework_04

import random #import library for useing random function
import string #import library for working with strings
import re # library for useing regex

def func_create_list (): # function for creation of list of dictionaries
    return [({random.choice(string.ascii_lowercase): random.randint(0, 100) for n in range(random.randint(1, 26))})  for m in range(random.randint(2, 10))]

res_list=func_create_list () # call the function and save the result in variable rez_list
print(f'Generated list of dictionaris:\n {res_list} \n') # print the created list of dictionaries

def func_create_dict (final_dict):
    for char in string.ascii_lowercase:
        temp_values = {}
        for i, next_dict in enumerate(res_list):
            if next_dict.get(char):
                temp_values[char + '_' + str(i + 1)] = next_dict.get(char)
        for key, value in temp_values.items():
            if len(temp_values) == 0:
                break
            elif len(temp_values) == 1:
                final_dict[
                    str(key)[0]] = value
            else:
                if value == max(temp_values.values()):
                    final_dict[key] = max(temp_values.values())
                    break
    return final_dict

print (f'Final dictionary with indexes:\n {func_create_dict (final_dict={})} \n') # print the final dictionary

str='''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''

def func_normalize(input_str, normilized_str):
    for sentence in re.sub(r'\t', '', re.sub(r'\n', '', input_str)).lower().split('.'):
        if re.search(r'\w', sentence):
            sentence = sentence.strip().capitalize() + sentence.strip()[1:] + '.\n'
        normilized_str += sentence
    return (normilized_str)

print (f'Normalized string is:\n {func_normalize(input_str=str, normilized_str="")} \n')

def func_new_sentence (input_str, new_sentence):
    for sentence in func_normalize(input_str=str, normilized_str="").split('.'):
        if re.search(r'\w', sentence):
            new_sentence += sentence.split()[-1] + ' '
    return func_normalize(input_str=str, normilized_str="")[:func_normalize(input_str=str, normilized_str="").find('paragraph.')+len('paragraph.')] + '\n' +\
                            new_sentence.capitalize() + '\n' + \
                            func_normalize(input_str=str, normilized_str="")[func_normalize(input_str=str, normilized_str="").find('paragraph.')+len('paragraph.')+1:]

print (f'Normalized string with new sentence is:\n {func_new_sentence (input_str=str, new_sentence="")} \n')

def func_fix_string():
    return re.sub(re.compile(' iz ', re.I), ' is ', func_new_sentence (input_str=str, new_sentence=""))

print (f'Fixed normilized string with new sentence:\n {func_fix_string()} \n')

def func_whitespaces_num(input_str):
    return len(re.findall(r'[\s]', input_str))

print (f'The number of whitespaces in initial string is:\n {func_whitespaces_num(input_str=str)} \n')
