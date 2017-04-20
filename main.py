import numpy as np
from table import createTable
from rulesets import get_Rulesets
from k_fold_cv import k_fold_cv


file = raw_input("Enter Filename: ")
approx = raw_input("Enter 1 for Lower Approximation or 2 for Upper Approximation: ")

while(approx not in ['1', '2']):
	approx = (raw_input("Enter 1 for Lower Approximation or 2 for Upper Approximation: "))

table, attributes = createTable(file)

Rulesets, Factors, support = get_Rulesets(table, attributes, approx)

error_rate = k_fold_cv(table, attributes, approx)




