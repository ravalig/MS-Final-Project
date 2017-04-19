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

def get_Rulesets(table, attributes, approx):

	d = table[:,-1]	
	d_star = defaultdict(list)
	for i, item in enumerate(d):
		d_star[item].append(i)
	d_star = {k:v for k,v in d_star.items()}

	concepts = d_star.keys()
	concept_cases = d_star.values()

	x = LEM2(table, attributes)

	Rulesets = []

	if(approx == '1'):
		LA = getLowerApprox(x.k_sets, concept_cases)
		for i in range(0, len(LA)):
			result = x.mlem2(LA[i])
			for r in result:
				Rulesets.append([r, [(attributes[-1],concepts[i])]])
	elif(approx == '2'):
		UA = getUpperApprox(x.k_sets, concept_cases)
		for i in range(0, len(UA)):
			result = x.mlem2(UA[i])
			for r in result:
				Rulesets.append([r, [(attributes[-1],concepts[i])]])

	Factors = []
	support = {}
	for rule in Rulesets:
		G = d_star[rule[1][0][1]]
		strength = len(x.get_intersection(rule[0]).intersection(G))
		specificity = len(rule[0])
		leftHand_av = len(x.get_intersection(rule[0]))
		Factors.append({'strength':strength, 'specificity':specificity, 'leftHand_av':leftHand_av})

		if(rule[-1][0] not in support.keys()):
			support[rule[-1][0]] = strength * specificity
		else:
			support[rule[-1][0]] = support[rule[-1][0]] + (strength * specificity)

	return Rulesets, Factors, support
	