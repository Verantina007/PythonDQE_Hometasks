import re # library for useing regex

input_str='''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''
# 1. Normalize the text

normilized_str = '' #new empty string for normilized string

for sentence in re.sub(r'\t', '', re.sub(r'\n', '', input_str)).lower().split('.'): # circle for list of sentences and make all elements in lower case
    if re.search(r'\w', sentence): # find the first letter in each sentence
        # make firest letter in each sentence capitalized and reasign element value
        sentence = sentence.strip().capitalize() + sentence.strip()[1:] + '.\n'
    normilized_str += sentence  # add reasigned element to normilized string and dot at the end of each sentence

# 2. Create a new sentence with last words of each existing sentence and add it at the end of the text

new_sentence = '' # empty string for new sentence

for sentence in normilized_str.split('.'): # circle for list of sentences and make all elements in lower case
    if re.search(r'\w', sentence): # find sentences with words
        new_sentence += sentence.split()[-1] + ' ' # add last word from each sentence in new_sentence

str_with_new_sentence = normilized_str[:normilized_str.find('paragraph.')+len('paragraph.')] + '\n' +\
                        new_sentence.capitalize() + '\n' + \
                        normilized_str[normilized_str.find('paragraph.')+len('paragraph.')+1:] # add new sentence in the end of the 3rd paragraph

#3. Fix 'IS' misspelling

fixed_string = re.sub(re.compile(' iz ', re.I), ' is ', str_with_new_sentence) # find all ' iz ' ignoring case and replace it with ' is '

# 4. Count the number of whitespaces
number_of_whitespaces = len(re.findall(r'[\s]', input_str)) # find all whitespaces and count the length of list with it

print(fixed_string) # print fixed string
print(f'The number of whitespaces in input_str is {number_of_whitespaces}') # print the number of whitespaces
