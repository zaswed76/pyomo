#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse

import math
from tabulate import tabulate

from pyomo import config
from pyomo.langlib import normal_form_file as omolib
import Levenshtein as lv
cfg = config.Config()

def sorter():
    pass

def printer(iterable, columns, tablefmt='plain'):
    """
    Various plain-text table formats (`tablefmt`) are supported:
    'plain', 'simple', 'grid', 'pipe', 'orgtbl', 'rst', 'mediawiki',
    'latex', 'latex_booktabs'.
     """
    size = int(math.ceil(len(iterable) / columns))
    iterable = [iterable[i:i+size] for i in range(0, len(iterable), size)]
    dict_iter = {_: i for _, i in enumerate(iterable)}
    print(tabulate(dict_iter, tablefmt=tablefmt))


def arg_parser(cfg):
    parser = argparse.ArgumentParser(
        description=''' поиск слов подобных по звучанию !!! ''')

    parser.add_argument('-r', dest='rating', default=cfg.rating, type=int,
                        help='''
                        рейтинг - целое число от 0 до 100
                        чем ниже рейтинг тем больше найденых слов''')

    parser.add_argument('-l', dest='limit_columns', default=cfg.limit_columns,
                        type=int,
                        help=''' колличество колонок (положительное целое число)
                        Колонок может быть меньше, но не может быть больше''')

    parser.add_argument('-s', dest='sort_key', default=cfg.sort_key,
                        type=int,
                        help=''' сортировать по  < n > первых букв''')

    parser.add_argument('-p', dest='prefix', default=cfg.prefix, type=float,
                        help='''
                        Compute Jaro string similarity metric of two strings.

                        The Jaro-Winkler string similarity metric is a
                        modification of Jaro metric giving more weight
                        to common prefix, as spelling mistakes are more
                        likely to occur near ends of words.

                        The prefix weight is inverse value of common prefix
                        length sufficient to consider the strings *identical*.
                        If no prefix weight is specified, 1/10 is used.''')


    return parser

diff_functions = dict(
    distance=lambda w, line: lv.distance(w, line),
    jaro_winkler=lambda w, line, pr: lv.jaro_winkler(w, line, pr),
    jaro=lambda w, line: lv.jaro_winkler(w, line),
    ratio=lambda w, line: lv.ratio(w, line)
)

def diff(fun, lst, word, ratio, *prefix):
    result = omolib.Accumulator()
    for line in lst:
        r = fun(line, word, *prefix)
        if r > ratio:
            result.append(line)
    return result

def main():
    parser = arg_parser(cfg)
    arg = parser.parse_args()
    default_rating = arg.rating
    default_prefix = arg.prefix
    limit_columns = arg.limit_columns
    sort_key = arg.sort_key
    dictionaries = omolib.Dictionaries(cfg)
    while True:
        repl = input('введите слово >>> \n').split(' ')
        # выход
        if repl[0] in ['Q', 'q', 'й', 'Й', 'exit']:
            print('Exit')
            sys.exit()
        else:
            try:
                word = repl[0].lower()
            except IndexError:
                print('Слово не введено.')
                continue
            try:
                default_rating = repl[1]
            except IndexError:
                pass


            ratio = float(default_rating)/100
            res = diff(diff_functions['jaro_winkler'],
                       dictionaries(), word,
                       ratio,
                       default_prefix)
            print(default_rating)
            res2 = omolib.Accumulator.sorted(res, word, sort_key)
            printer(res2, limit_columns)


if __name__ == '__main__':
    main()
