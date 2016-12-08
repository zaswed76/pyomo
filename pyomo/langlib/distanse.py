# -*- coding: utf-8 -*-
from collections import OrderedDict

import Levenshtein as lv
import paths

from pyomo.langlib import normal_form_file as file_lib

from difflib import SequenceMatcher

def pprint(seq):
    for i in seq:
        print(i)
        print('-------------------')
    print(len(seq))

def func4(lst, word, r):
    result = []
    for line in lst:
        if SequenceMatcher(None, line, word).ratio() > r:
            result.append(line)
    return result


diff_functions = dict(
    distance=lambda w, line: lv.distance(w, line),
    jaro_winkler=lambda w, line, pr: lv.jaro_winkler(w, line, pr),
    jaro=lambda w, line: lv.jaro_winkler(w, line),
    ratio=lambda w, line: lv.ratio(w, line),
    difflib=lambda w, line: SequenceMatcher(None, line, w).ratio()
)


def diff(fun, lst, word, ratio, *prefix):
    result = set()
    for line in lst:
        if fun(line, word, *prefix) > ratio:
            result.add(line)
    return result




if __name__ == '__main__':
    w = 'аплик'
    w2 = 'тебл***'
    lst = file_lib.file_to_words(paths.dict_work('result.txt'))

    # print(diff(diff_functions['ratio'],lst, w, 0.75))

    ratio = 0.85
    ratio_step = 0.01
    dct = OrderedDict()
    ak = set()
    for _ in range(100):
        res = diff(diff_functions['jaro_winkler'],lst, w, ratio, 0.1)
        if res:
            if ak:
                res = res - ak
            ak.update(res)
            if res:
                dct[ratio] = sorted(list(res))
            ratio -= ratio_step
            if len(res) > 100:
                break
    pprint(dct.values())
    # print(func2(lst, w, 3))
    # print('------------------')
    # print(func3(lst, w, 0.64))
    # # print(func(lst, w2, 4))
