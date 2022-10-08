# Homework_04

import random #import library for useing random function
import string #import library for working with strings
import re # library for useing regex

#2nd module task
#define functions:
def create_list_of_dict (num_list_elements): # function for creation of list of dictionaries with len n
    return [({random.choice(string.ascii_lowercase): random.randint(0, 100) for m in range(random.randint(1, 26))})  for i in range(num_list_elements)]

def create_dict_from_list (input_list_of_dict): # function for creation one final dictionary from alldictionaries in the list
    final_dict={}
    for char in string.ascii_lowercase:
        temp_values = {}
        for i, next_dict in enumerate(input_list_of_dict):
            if next_dict.get(char):
                temp_values[char + '_' + str(i + 1)] = next_dict.get(char)
        for key, value in temp_values.items():
            if len(temp_values) == 0:
                break
            elif len(temp_values) == 1:
                final_dict[str(key)[0]] = value
            else:
                if value == max(temp_values.values()):
                    final_dict[key] = max(temp_values.values())
                    break
    print (f'Created list with dict is:\n{input_list_of_dict}\nFinal dictionary is:\n{final_dict}\n')

# call function for creation final dictionary where argument is another function returning list of dictionaries
create_dict_from_list (input_list_of_dict = create_list_of_dict (num_list_elements = random.randint(2, 10)))

#3rd module task
#define functions:
def normalize_string (str_for_normalization): # function for normalization of the string
    normalized_str=''
    for sentence in re.sub(r'\t', '', re.sub(r'\n', '', input_str)).lower().split('.'):
        if re.search(r'\w', sentence):
            sentence = sentence.strip().capitalize() + '.\n'
            normalized_str += sentence
    return normalized_str

def add_new_sentence (str_for_adding): # function for adding a new sentence
    new_sentence=''
    for sentence in str_for_adding.split('.'):
        if re.search(r'\w', sentence):
            new_sentence += sentence.split()[-1] + ' '
    str_with_new_sentence=str_for_adding[:str_for_adding.find('paragraph.')+len('paragraph.')] + '\n' +\
                            new_sentence.strip().capitalize() + '.\n' + \
                            str_for_adding[str_for_adding.find('paragraph.')+len('paragraph.')+1:]
    return str_with_new_sentence

def fix_iz_in_string (str_for_fixes): # function for fixing not correct 'iz'
    return re.sub(re.compile(' iz ', re.I), ' is ', str_for_fixes)

def count_whitespaces (str_for_counting): # function for count the whitespaces
    return len(re.findall(r'[\s]', str_for_counting))

input_str='''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''

#call functions for getting necessary results
print (normalize_string (str_for_normalization = input_str)) # normalize input string
print (add_new_sentence (str_for_adding = normalize_string (str_for_normalization = input_str))) #add new sentence in normalized string
print (fix_iz_in_string (str_for_fixes = normalize_string (str_for_normalization = input_str))) #fix incorrect 'iz' in normalized string
print (fix_iz_in_string (add_new_sentence (str_for_adding = normalize_string (str_for_normalization = input_str)))) #fix incorrect 'iz' in normalized string with new sentence
print (count_whitespaces (str_for_counting = input_str)) # count number of whitespaces in input string
print (count_whitespaces (fix_iz_in_string (add_new_sentence (str_for_adding = normalize_string (str_for_normalization = input_str))))) # count whitespaces in normalized string with new sentence
