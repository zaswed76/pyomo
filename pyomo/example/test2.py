# -*- coding: utf-8 -*

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

    def append(self, p_object):
        if not p_object in self:
            super().append(p_object)
        else:
            print('not append')

lst = Accumulator(50)
lst.append(1)
lst.append(2)
lst.append(1)
print(lst)




