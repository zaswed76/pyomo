# -*- coding: utf-8 -*-

from pprint import pprint
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
def printer(seq):
    for i in seq:
        for x in i:
            print(x)
        print('--------------------')

word = 'стол'
pars = morph.parse(word)
pars2 = morph.parse(word)[1]

printer(pars)