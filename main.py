import numpy as np
from table import createTable
from attr_value_pairs import get_av_pairs
from characteristics_sets import get_characteristic_sets
from lem2 import get_TG, mlem2, get_intersection

from collections import defaultdict

file = 'input1.txt'

table, attributes = createTable(file)

decisions = table[:,-1]

av_pairs = get_av_pairs(attributes, table)

k_sets = get_characteristic_sets(attributes, table, av_pairs)

B=[0, 1 ,2]


RuleSets = mlem2(av_pairs, B)
