import random
import numpy as np
from rulesets import get_Rulesets
from sklearn.model_selection import KFold

def k_fold_cv(table, attributes, approx):
	np.random.shuffle(table)
	kf = KFold(n_splits = 3)
	
	for trainIndex, testIndex in kf.split(table): 
		print("TRAIN:", trainIndex, "TEST:", testIndex)
		trainData, testData = table[trainIndex], table[testIndex]
		Rulesets, Factors, support = get_Rulesets(trainData, attributes, approx)
		
		for i in range(0, len(Rulesets)):
			print(Rulesets[i])
			print(Factors[i])
		print('\n')
	return None