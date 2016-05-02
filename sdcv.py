#!/usr/bin/env python3

import re
from pystardict import Dictionary
from pathlib import Path

def trans_words_list():
    # ---------- loading all the dictionaries ----------
    dictionaries = []
    dict_path_prefix = Path.home().joinpath('.stardict')
    for i_dir in dict_path_prefix.glob('*'):
        dict_path = dict_path_prefix.joinpath(i_dir)
        dict_dir_name = str(dict_path) + '/'
        for dict_name in dict_path.glob('*'):
            if dict_name.match('*.ifo'):
                info_name = dict_name.stem
            if dict_name.match('*.idx'):
                indx_name = dict_name.stem
            if dict_name.match('*.dict') or dict_name.match('*.dict.dz'):
                data_name = dict_name.stem.split('.')[0]
        if not info_name == indx_name == data_name:
            print('Error: Dictionary name should be same for .ifo .idx and .dict (.dict.dz) files.')
            return 0
        else:
            dict_name = dict_dir_name + data_name
            dict1 = Dictionary(dict_name, True)
            dictionaries.append(dict1)

    # ---------- output string format ----------
    indexword_out_str = '[0;32;1m{0}[0m'

    print('[0;30;1m==========================================================================================[0m')
    while True:
        try:
            request = input('[0;30;1m Input: [0m')
        except Exception:
            return 0
        for d in dictionaries:
            dict_key_list = d.keys()
            for dict_word in dict_key_list:
                if request == dict_word:
                    translation = d[dict_word]
                    print('------------------------------')
                    print(indexword_out_str.format(dict_word))
                    print(translation)
        print('[0;30;1m==========================================================================================[0m')

if __name__ == '__main__':
    trans_words_list()
    
