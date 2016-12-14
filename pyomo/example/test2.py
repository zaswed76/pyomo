# -*- coding: utf-8 -*

iterable = list(range(11))
count = 3
from tabulate import tabulate


def chunks(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in
            range(0, len(lst), chunk_size)]


res = chunks(iterable, 5)


def printer(iterable, size):
    iterable = [iterable[i:i + size] for i in
                range(0, len(iterable), size)]
    dict_iter = {_: i for _, i in enumerate(iterable)}
    print(tabulate(dict_iter))


res3 = ['лов', 'саловар', 'силовой', 'словак', 'словарик', 'сов', 'Маслов', 'слякоть']


def sorter(iterable, original, cletter=1):
    a_lst = []
    b_lst = []
    for i in iterable:
        if i.startswith(original[0:cletter]):
            a_lst.append(i)
        else:
            b_lst.append(i)
    a_lst.extend(b_lst)
    return a_lst

class Accumulator(list):
    def __init__(self):
        super().__init__()

    def uniq_append(self, p_object):
        if not p_object in self:
            super().append(p_object)

    def uniq_extend(self, iterable):
        super().extend([x for x in iterable if x not in self])

    @staticmethod
    def sorted(iterable, original, cletter):
        ac = Accumulator()
        s = reversed(range(1, cletter+1))
        for n in s:
            ac.uniq_extend([x for x in iterable if x.startswith(original[0:n])])
        ac.uniq_extend(iterable)
        return ac



print(Accumulator.sorted(res3, 'слово', 3))