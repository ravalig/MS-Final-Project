import numpy as np
from table import createTable
from attr_value_pairs import calculate_av_pairs, add_to_avpair

file = 'input1.txt'

table, attributes = createTable(file)


calculate_av_pairs(attributes, table)


