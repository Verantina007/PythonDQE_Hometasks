input_str='''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''

import re # library for useing regex

# 1. Normalize the text

normilized_str = '' #new empty string for normilized string

for element in input_str.lower().split('.'): # circle for list of sentences and make all elements in lower case
    if re.search(r'[a-z]', element): # find the first letter in each sentence
        # make firest letter in each sentence capitalized and reasign element value
        element = element[0:re.search(r'[a-z]', element).start()]+\
                  element[re.search(r'[a-z]', element).start()].capitalize()+\
                  element[re.search(r'[a-z]', element).start()+1:]
        normilized_str += element + '.' # add reasigned element to normilized string and dot at the end of each sentence
    else:
        normilized_str += '\n' # add element if there are no letters in the sentence

print ('1. Normilizwd string is: \n', normilized_str) # print the normilized sentence

# 2. Create a new sentence with last words of each existing sentence and add it at the end of the text

new_sentence = '' # empty string for new sentence

for element in input_str.lower().split('.'): # circle for list of sentences and make all elements in lower case
    if re.search(r'[a-z]', element): # find sentences with words
        new_sentence += element.split()[-1] + ' ' # add last word from each sentence in new_sentence

str_with_new_sentence = normilized_str + ' ' + new_sentence[0].capitalize() + new_sentence[1:] # add new sentence in the input string
print ('2. String with new sentence is: \n', str_with_new_sentence) # print string with new sentence

#3. Fix 'IS' misspelling
#while re.findall(r' iz ', str_with_new_sentence, re.I):

fixed_string = re.sub(re.compile(' iz ', re.I), ' is ', str_with_new_sentence) # find all ' iz ' ignoring case and replace it with ' is '
print('3. Fixed string is: \n', fixed_string) # print fixed string

# 4. Count the number of whitespaces
n = len(re.findall(r'[ \t\n\r\f\v]', input_str)) # find all whitespaces and count the length of list with it
print('4. The number of whitespaces is: \n', n) # print the number of whitespaces
