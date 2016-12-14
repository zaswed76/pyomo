import math
from tabulate import tabulate
import tabulate as tb

def printer(iterable, columns, tablefmt='plain'):
    """
    Various plain-text table formats (`tablefmt`) are supported:
    'plain', 'simple', 'grid', 'pipe', 'orgtbl', 'rst', 'mediawiki',
    'latex', 'latex_booktabs'.
     """
    size = int(math.ceil(len(iterable) / columns))
    print(size)
    iterable = [iterable[i:i+size] for i in range(0, len(iterable), size)]
    dict_iter = {_: i for _, i in enumerate(iterable)}
    print(tabulate(dict_iter, tablefmt=tablefmt))


lst = range(6)

printer(lst, 4, 'simple')