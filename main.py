import numpy as np
from table import createTable
from lem2 import LEM2
# from collections import defaultdict

file = 'input1.txt'

table, attributes = createTable(file)

x = LEM2(table, attributes)

B=[0, 1 ,2]
print(x.mlem2(B))


# RuleSets = mlem2(av_pairs, B)
