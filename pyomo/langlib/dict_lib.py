#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import _chain, OrderedDict

class Dictionaries:
    Noun = 'noun'
    Verb = 'verb'
    Adj = 'adj'
    Names = 'names'
    Other = 'other'
    def __init__(self, **dictionaries):
        """


        :param cfg:
        """
        self.seq = [self.Noun, self.Adj, self.Verb, self.Names, self.Other]
        self.dictionaries = dict(dictionaries)

    def __call__(self, *args):
        if args:
            seq = args
        else:
            seq = self.seq
        lst = []
        for k in seq:
            try:
                lst.extend(self.dictionaries[k])
            except: pass
        return lst


if __name__ == '__main__':
    n = [1,2]
    v = [3,4]
    a = [5,6]
    name = [5,6]
    o = [5,6]
    d = Dictionaries(noun=n)
    print(d())