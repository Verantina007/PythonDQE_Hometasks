import re  # library for useing regex

def normalize_string(str_for_normalization):  # function for normalization of the string
    normalized_str = ''
    for sentence in re.sub(r'\t', '', re.sub(r'\n', '', str_for_normalization)).lower().split('.'):
        if re.search(r'\w', sentence):
            sentence = sentence.strip().capitalize() + '.\n'
            normalized_str += sentence
    return normalized_str
