# -*- coding: utf-8 -*-

from pprint import pprint
import pymorphy2
morph = pymorphy2.MorphAnalyzer()




pprint(morph.parse('стали'))