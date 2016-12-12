# -*- coding: utf-8 -*-
from collections import OrderedDict
from tabulate import tabulate
import Levenshtein as lv
import paths
from langlib import normal_form_file as file_lib


class Accumulator(list):
    def __init__(self, limit):
        super().__init__()
        self.limit = limit

    def extend_(self, iterable):
        super().extend(iterable)
        temp = self.copy()
        self.clear()
        self.extend(temp[:self.limit])
        return temp[self.limit:]

class MyDict(OrderedDict):
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)

    def __len__(self):
        s = 0
        for x in self.values():
            s += len(x)
        return s




def pprint(seq):
    for k, v in seq.items():
        print(round(k, 3), v, sep=' = \n')
        print('-------------------')
    print(len(seq))



diff_functions = dict(
    distance=lambda w, line: lv.distance(w, line),
    jaro_winkler=lambda w, line, pr: lv.jaro_winkler(w, line, pr),
    jaro=lambda w, line: lv.jaro_winkler(w, line),
    ratio=lambda w, line: lv.ratio(w, line)
)


def diff(fun, lst, word, ratio, *prefix):
    result = set()
    for line in lst:
        r = fun(line, word, *prefix)
        if r > ratio:
            if line == 'апликация':
                print(r, 'апликация')
            result.add(line)
    return result

def main():
    empty = 0
    word = 'еплик'
    lst = file_lib.file_to_words(paths.dict_work('result_not_dubble.txt'))
    ratio = 0.85
    ratio_step = 0.02
    limit = 50
    dct = MyDict()
    ak = set()
    for _ in range(40):
        res = diff(diff_functions['jaro_winkler'], lst, word, ratio, 0.1)
        if res:
            if ak:
                res = res - ak
            ak.update(res)
            if res:
                dct[round(ratio, 3)] = sorted(list(res))


            if len(res) > limit:
                break
            ratio -= ratio_step
        else:
            ratio -= ratio_step
            empty += 1
            continue

    print(tabulate(dct, headers='keys'))
    print(len(dct))



if __name__ == '__main__':
    main()


