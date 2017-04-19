import numpy as np
from table import createTable
from rulesets import get_Rulesets
import random

file = raw_input("Enter Filename: ")
table, attributes = createTable(file)

approx = raw_input("Enter 1 for Lower Approximation or 2 for Upper Approximation: ")

while(approx not in ['1', '2']):
	approx = (raw_input("Enter 1 for Lower Approximation or 2 for Upper Approximation: "))

if(approx == '1'):
	Rulesets, Factors, support = get_Rulesets(table, attributes, approx)
elif(approx == '2'):
	Rulesets, Factors, support = get_Rulesets(table, attributes, approx)


# np.random.shuffle(table)

