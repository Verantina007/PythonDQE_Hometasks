# Homework_02

# 1. create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

import random #import library for useing random function
import string #import library for working with strings

n = random.randint (2, 10) # length of list with dictionaries

res_list=[] # empty list for adding disctionaries

for i in range(n): # circle for the number of elements in list
    m=random.randint (1, 26) # generate the number of key-value pairs in each dictionary in res_list
    temp_dict={} # temporary dictionary for adding each dictionary that will be an element of res_list
    for j in range (m): # circle for the number of elements for each dictionary
        temp_dict[random.choice(string.ascii_lowercase)] = random.randint (0, 100) # generate key-value pair for the dictionary
        #can be the same random values for keys, so we can have less key-value pairs then we have in m
    res_list.append(temp_dict) # append generated dictionary in the list

print(res_list)

# 2. get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

# checking res_list=[{'a':1, 'b':2, 'c':3}, {'a':1, 'b':2, 'c':3}, {'a':1, 'b':2, 'c':3}]

final_dict = {} # final dictionary for adding the result

for char in string.ascii_lowercase: # go through all letters in the alphabet
    temp_values={} # temporary dictionary for each letter with the number of dictionary and value for this key
    for i in range(n): # circle through all dictionaries in the list
        if res_list[i].get(char) is not None: # exclude None values - letters that do not exist in dictionary
            temp_values[char+'_'+str(i+1)]=res_list[i].get(char) # add number of dictionary for the letter and value for this key
    for key, value in temp_values.items(): # circle through temporary dictionary for each letter
        if value==max(temp_values.values()): # choose only key-value pair with max value for each letter
            final_dict[key]=value # add the key-value pair in final_dict
            break# skip duplicated values, take only the first one

print (final_dict ) # print the result
