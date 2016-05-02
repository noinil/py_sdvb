#!/usr/bin/env python3

import re
from pystardict import Dictionary

def trans_words_list(regex):
    dict1 = Dictionary('dicts/CET4', True)

    indexword_out_str = '[0;32;1m{0}[0m'

    wordlist = []
    search_reg = re.compile(regex)
    dict_key_list = dict1.keys()
    for dict_word in dict_key_list:
        result = re.search(search_reg, dict_word)
        if result:
            wordlist.append(dict_word)
            translation = dict1[dict_word]
            print('------------------------------')
            print(indexword_out_str.format(dict_word))
            print(translation)
            print('')

if __name__ == '__main__':
    regex = input('REGEX: ')
    trans_words_list(regex)
    
