#!/usr/bin/env python3

import re
from pystardict import Dictionary
from pathlib import Path
import sys

def translate_words_list(sel_dict):
    # ---------- loading all the dictionaries ----------
    dictionaries = []
    dict_book_names = []
    dict_path_prefix = Path.home().joinpath('.stardict')
    for i_dir in dict_path_prefix.glob('*'):
        dict_path = dict_path_prefix.joinpath(i_dir)
        dict_dir_name = str(dict_path) + '/'
        for dict_name in dict_path.glob('*'):
            if dict_name.match('*.ifo'):
                info_name = dict_name.stem
                with open(str(dict_name), 'r') as dict_info_file:
                    for line in dict_info_file:
                        if line.startswith('bookname'):
                            words = line.strip().split('=')
                            dict_book_names.append(words[-1])
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

    # ---------- dictionary selection if sel_dict == 1 ----------
    if sel_dict == 1:
        print(' Please select a dictionary: ')
        dicsel_str = ' ({0}) - {1}'
        for i_dict, dname in enumerate(dict_book_names):
            print(dicsel_str.format(i_dict, dname))
        i_chosen = int(input(' Input a number: '))
        try:
            d_tmp = dictionaries[i_chosen]
            dictionaries = [d_tmp]
            name_tmp = dict_book_names[i_chosen]
            dict_book_names = [name_tmp]
        except Exception:
            print(" Dictionary selection error.")
            print(" Trying to use all the dictionaries!")
        print("------------------------------")
    

    # ---------- output string format ----------
    indexword_out_str = '[0;32;1m{0}[0m'
    pos_out_str = ' [1;36;2m{0}[1;37;1m{1}[0m'
    pos_cn_out_str = ' [0;35;2m{0}[0m{1}'
    phon_out_str = ' [0;30;1m{0}[0m'
    misc_out_str = ' [0;31;2m{0}[0m'
    dict_name_out_str = ' [1;34;1m{0}[0m'

    # regular expressions
    pos_reg = re.compile('(a|v|n|ad|adj|adv|vt|vi)\.')
    pos_cn_reg = re.compile('【.*】')
    phon_reg = re.compile('\*?\[.*\]')
    pinyin_bug = re.compile('([a-z]\?.*){2,}')
    jap_bug = re.compile('\$')

    # searching loop...
    print('[0;30;1m==========================================================================================[0m')
    while True:
        try:
            regex = input('REGEX: ')
        except Exception:
            return 0
        for i, d in enumerate(dictionaries):
            search_reg = re.compile(regex)
            dict_key_list = d.keys()
            for dict_word in dict_key_list:
                result = re.search(search_reg, dict_word)
                if result:
                    translation = d[dict_word]
                    print('[0;30;1m--------------------------------------------------[0m')
                    print(dict_name_out_str.format(dict_book_names[i]))
                    print(indexword_out_str.format(dict_word))
                    for transline in translation.split('\n'):
                        m_pos = re.match(pos_reg, transline)
                        m_pos_cn = re.search(pos_cn_reg, transline)
                        if m_pos:
                            print(pos_out_str.format(transline[:m_pos.end()], transline[m_pos.end():]))
                        elif m_pos_cn:
                            print(pos_cn_out_str.format(transline[:m_pos_cn.end()], transline[m_pos_cn.end():]))
                        elif re.match(phon_reg, transline):
                            print(phon_out_str.format(transline))
                        elif transline.startswith('词形') or transline.startswith('例句') or transline.startswith('相关'):
                            print('[0;30;1m~~~~~~~~~~~~~~~~~~~~[0m')
                            print(misc_out_str.format(transline))
                        elif re.match(pinyin_bug, transline):
                            pass
                        elif jap_bug.match(transline):
                            print('  ', transline[1:])
                        else:
                            print(' ', transline)
        print('[0;30;1m==========================================================================================[0m \n')

def select_dictionary():
    sdo = 0
    if len(sys.argv) > 1:
        sel_dict_opt = sys.argv[1]
        if sel_dict_opt == '-h':
            print(' USAGE: ', sys.argv[0], ' [-s] [-h]')
            print('        -s: select dictionary;')
            print('        -h: help.')
            exit(0)
        elif sel_dict_opt == '-s':
            sdo = 1

    translate_words_list(sdo)
    

if __name__ == '__main__':
    select_dictionary()
