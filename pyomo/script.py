#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
from pyomo import paths
from pyomo import config
from pyomo.langlib import distanse
from pyomo.langlib import normal_form_file as file_lib
from pyomo.langlib import dict_lib

cfg = config.Config()

def arg_parser():
    parser = argparse.ArgumentParser(
            description=''' поиск слов подобных по звучанию
            ''')
    parser.add_argument('цщкв',
                        help='путь к миниаюре', type=str)

    return parser



def main():
    dictionaries = file_lib.Dictionaries(cfg)
    repl = ''
    while True:
        repl = input('введите слово\n')
        # выход
        if repl in ['Q', 'q']:
            print('Exit')
            sys.exit()
        else:
            pass





if __name__ == '__main__':
    main()