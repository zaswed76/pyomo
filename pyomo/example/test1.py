# -*- coding: utf-8 -*-

from  collections import OrderedDict

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




class UserDict(OrderedDict):
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)


        self.accamulator = []


if __name__ == '__main__':
    lst = Accumulator(5)
    pop = lst.extend_([1,2,3,4,5,6])
    print(lst)
    print(pop)