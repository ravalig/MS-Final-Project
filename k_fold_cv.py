import random
import numpy as np
from collections import defaultdict
from rulesets import get_Rulesets
from testdata_avpairs import get_av_pairs1
from sklearn.model_selection import KFold

def k_fold_cv(table, attributes, approx, k):
	np.random.shuffle(table)
	kf = KFold(n_splits = int(k))
	
	av_pairs1 = get_av_pairs1(attributes, table)
	errors=0
	for trainIndex, testIndex in kf.split(table): 
		#print("TRAIN:", trainIndex, "TEST:", testIndex)
		trainData, testData = table[trainIndex], table[testIndex]
		Rulesets, Factors, support = get_Rulesets(trainData, attributes, approx)
		
		d =[]
		for r in range(0, len(Rulesets)):
			d.append(Rulesets[r][1][0][1])
		
		for testcase_index in testIndex:    # For each test case
			matching_rules = []
			exactmatch=False
			decision_support = {}
			decision_partial_support = {}
			for dec in d:
				if(dec not in decision_support.keys()):
					decision_support[dec] = 0
				if(dec not in decision_partial_support.keys()):	
					decision_partial_support[dec] = 0

			for r in range(0, len(Rulesets)):	# For each rule

				m = len(av_pairs1[testcase_index].intersection(set(Rulesets[r][0])))
				mf = float(m)/float(Factors[r]['specificity'])
				if(mf == 1 ):
					exactmatch=True
					support = (Factors[r]['specificity'] * Factors[r]['strength'] )
					decision_support[Rulesets[r][1][0][1]] = decision_support[Rulesets[r][1][0][1]] + support
				else:
					partial_support = (Factors[r]['specificity'] * Factors[r]['strength'] )
					decision_partial_support[Rulesets[r][1][0][1]] = decision_partial_support[Rulesets[r][1][0][1]] + partial_support
				
			prediction=""
			if(exactmatch):
				ind = decision_support.values().index(max(decision_support.values()))
				prediction = decision_support.keys()[ind]
			else:
				ind = decision_partial_support.values().index(max(decision_partial_support.values()))
				prediction = decision_partial_support.keys()[ind]
			original = table[testcase_index][-1]
			if(prediction!=original):
				errors = errors + 1

	error_rate = float(errors)/float(len(table))
	
	return error_rate