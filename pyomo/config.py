# -*- coding: utf-8 -*-

class Config:
    def __init__(self):
        self.dictionaries = dict(
            noun='no_duplicate_letters.txt',
            verb='',
            adj='',
            names='name.txt',
            other='',
        )
        self.noun_dict = True
        self.verb_dict = True
        self.adjective_dict = True
        self.names_dict = True
        self.other_dict = True