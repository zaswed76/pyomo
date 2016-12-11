#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyomo import paths
from pyomo import config
from pyomo.langlib import distanse
from pyomo.langlib import normal_form_file as file_lib
from pyomo.langlib import dict_lib

cfg = config.Config()

def get_dictionaries():
    dictionaries = {}
    for name, dct in cfg.dictionaries.items():
        dictionaries[name] = file_lib.file_to_words(paths.dict_work(cfg.dictionaries[dct]))
    return dictionaries



def main():
    dictionaries = get_dictionaries()
    print(dictionaries)
    # work_words = dict_lib.Dictionaries()



if __name__ == '__main__':
    main()