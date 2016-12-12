#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
import paths
import config
from langlib import distanse
from langlib import normal_form_file as file_lib
from langlib import dict_lib

cfg = config.Config()


def arg_parser():
    parser = argparse.ArgumentParser(
        description=''' поиск слов подобных по звучанию
            ''')

    parser.add_argument('-r', dest='rating', default=85, type=int,
                        help='''
                        рейтинг - целое число от 0 до 100
                        чем ниже рейтинг тем больше найденых слов''')
    parser.add_argument('-m', dest='max', default=150, type=int,
                        help='''
                        максимальное число найденных слов - целое число
                         от 0 до 2000 (0 и 2000 - условные величины)
                        ''')
    return parser


def main():
    parser = arg_parser()
    arg = parser.parse_args()
    default_rating = arg.rating
    default_max = arg.max
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
