# -*- coding: utf-8 -*

iterable = list(range(11))
count = 3


def f(iterable, limit):
    a = []
    lst = []
    for i in iterable:
        lst.append(i)
        if len(lst) == limit:
            a.append(lst)
            lst = lst.copy()
            lst.clear()



    return a

print(f(iterable,  4))






