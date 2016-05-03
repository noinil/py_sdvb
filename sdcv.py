#!/usr/bin/env python3

from pystardict import Dictionary
from pathlib import Path
import re

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
    pos_out_str = '[0;37;1m{0}[0m'
    phon_out_str = '[0;30;1m{0}[0m'
    misc_out_str = '[0;36;1m{0}[0m'

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
                    print('[0;30;1m--------------------------------------------------[0m')
                    print(indexword_out_str.format(dict_word))
                    # print(translation)
                    for transline in translation.split('\n'):
                        pos_reg = re.compile('(a|v|n|adj|adv|vt|vi)\.')
                        phon_reg = re.compile('\*?\[.*\]')
                        if re.match(pos_reg, transline):
                            print(pos_out_str.format(transline))
                        elif re.match(phon_reg, transline):
                            print(phon_out_str.format(transline))
                        elif transline.startswith('词形') or transline.startswith('例句') or transline.startswith('相关'):
                            print('[0;30;1m--------------------[0m')
                            print(misc_out_str.format(transline))
                        else:
                            print(transline)

        print('[0;30;1m==========================================================================================[0m')

if __name__ == '__main__':
    trans_words_list()
    
