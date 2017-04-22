import numpy as np
from table import createTable
from rulesets import get_Rulesets
from k_fold_cv import k_fold_cv

file = raw_input("Enter Filename: ")
table, attributes = createTable(file)

k = int(raw_input("Enter number of folds: "))
while( k < 2 or k >= len(table)):
	print("K value should be between 2 and " + str(len(table)-1))
	k = raw_input("Enter number of folds: ")

approx = raw_input("Enter 1 for Lower Approximation or 2 for Upper Approximation: ")
while(approx not in ['1', '2']):
	approx = (raw_input("Enter 1 for Lower Approximation or 2 for Upper Approximation: "))

output_file = raw_input("Enter output file name: ")

Rulesets, Factors, support = get_Rulesets(table, attributes, approx)
error_rate = k_fold_cv(table, attributes, approx, k)

f = open(output_file, 'w')
for r in range(0, len(Rulesets)):
	if(len(Rulesets[r][0]) == 1):
		f.write('('+str(Factors[r]['specificity']) + ', ' + str(Factors[r]['strength']) + ', ' + str(Factors[r]['leftHand_av']) + ')')
		f.write('\n')
		line = str(Rulesets[r][0][0]) + ' -> ' + str(Rulesets[r][1][0])
		f.write(line)
		f.write('\n')
		
	else:
		f.write('('+ str(Factors[r]['specificity']) + ', ' + str(Factors[r]['strength']) + ', ' + str(Factors[r]['leftHand_av']) + ')')
		f.write('\n')
		for i in range(0, len(Rulesets[r][0])-1):
			f.write(str(Rulesets[r][0][i]) + ' & ')
		f.write(str(Rulesets[r][0][-1]))
		f.write(' -> ' + str(Rulesets[r][1][0]))
		f.write('\n')
	
f.close()

print("error rate :", error_rate)



