# -*- coding: utf-8 -*-

from Levenshtein import distance, jaro, jaro_winkler
import paths


from pyomo.langlib import normal_form_file as file_lib

def func(lst, word, r):
    result = []
    for line in lst:
        if distance(word, line) == r:
            result.append(line)
    return result

def func2(lst, word, r):
    result = []
    for line in lst:
        if jaro_winkler(word, line, 0.1) > 0.83:
            result.append(line)
    return result

if __name__ == '__main__':
    w = 'консайде'
    w2 = 'тебл***'
    lst = file_lib.file_to_words(paths.dict_work('result.txt'))
    # print(func(lst, w, 1))
    # print(func(lst, w, 2))
    # print('-----------------------')
    print(func2(lst, w, 1))
    # print(func(lst, w2, 2))
    # print(func(lst, w2, 3))
    # print(func(lst, w2, 4))
