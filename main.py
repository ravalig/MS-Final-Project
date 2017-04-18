import numpy as np
from table import createTable
from rulesets import get_Rulesets
import random

file = 'input2.txt'
table, attributes = createTable(file)
Certain_Rulesets, Possible_Rulesets = get_Rulesets(table, attributes)

for cr in Certain_Rulesets:
	print(cr)

print('\n')

for pr in Possible_Rulesets:
	print(pr)

# np.random.shuffle(table)

