from collections import defaultdict
from lem2 import LEM2

def getLowerApprox(k_sets, concept_cases):
	LA = []
	for X in concept_cases:
		result = []
		for x in X:
			if(k_sets[x].issubset(X)):
				result = set(result).union(k_sets[x])
		LA.append(result)
	return LA

def getUpperApprox(k_sets, concept_cases):
	UA = []
	for X in concept_cases:
		result = []
		for x in X:
			result = set(result).union(k_sets[x])
		UA.append(result)
	return UA

def get_Rulesets(table, attributes):

	d = table[:,-1]	
	d_star = defaultdict(list)
	for i, item in enumerate(d):
		d_star[item].append(i)
	d_star = {k:v for k,v in d_star.items()}

	concepts = d_star.keys()
	concept_cases = d_star.values()

	Certain_Rulesets = []
	Possible_Rulesets = []

	x = LEM2(table, attributes)

	LA = getLowerApprox(x.k_sets, concept_cases)
	UA = getUpperApprox(x.k_sets, concept_cases)

	for i in range(0, len(LA)):
		result = x.mlem2(LA[i])
		for r in result:
			Certain_Rulesets.append([r, concepts[i]])

	for i in range(0, len(UA)):
		result = x.mlem2(UA[i])
		for r in result:
			Possible_Rulesets.append([r, concepts[i]])

	return Certain_Rulesets, Possible_Rulesets