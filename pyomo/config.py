# -*- coding: utf-8 -*-

class Config:
    def __init__(self):
        self.dictionaries = dict(
            noun='no_duplicate_letters.txt',
            verb='',
            adj='',
            names='name.txt',
            other=''
        )
        self.init_dictionaries = dict(
            noun=True,
            verb=False,
            adj=False,
            names=True,
            other=True
        )

        ''' int min 0 max 99 '''
        self.rating = 87

        ''' float min 0.1; max 1.0 '''
        self.prefix = 0.1

        ''' колличество слов в столбце'''
        self.word_limit_column = 40


        '''
        СОРТИРОВАТЬ по первым буквам
        Вначале идут слова в которых совпадают первые 3 буквы,
        затем первые 2 буквы,
        затем первая буква,
        затем все остальные
        список повторов не содержит
        '''
        self.sort_key = 3
