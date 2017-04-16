import numpy as np
from table import createTable
from attr_value_pairs import get_av_pairs
from characteristics_sets import get_characteristic_sets

file = 'input1.txt'

table, attributes = createTable(file)

av_pairs = get_av_pairs(attributes, table)

k_sets = get_characteristic_sets(attributes, table, av_pairs)

