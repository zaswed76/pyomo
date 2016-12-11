#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyomo import paths
from pyomo import config
from pyomo.langlib import distanse
from pyomo.langlib import normal_form_file as file_lib
from pyomo.langlib import dict_lib

cfg = config.Config()





def main():
    dictionaries = file_lib.Dictionaries(cfg)
    print(dictionaries())
    # work_words = dict_lib.Dictionaries()



if __name__ == '__main__':
    main()