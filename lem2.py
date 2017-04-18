from collections import defaultdict

def get_t(TG, av_pairs, G, T):
	T_temp = []
	for l in T:
		T_temp.append(l[0])

	relevance = []
	cardinality = []
	for av in TG:
		relevance.append(len(av_pairs[av].intersection(set(G))))
		cardinality.append(len(av_pairs[av]))
	
	D_rel = defaultdict(list)
	for i,item in enumerate(relevance):
		D_rel[item].append(i)
	D_rel = {k:v for k,v in D_rel.items()} 

	D_card = defaultdict(list)
	for i,item in enumerate(cardinality):
		D_card[item].append(i)
	D_card = {k:v for k,v in D_card.items()} 

	max_val = max(relevance)
	max_rel_index = D_rel[max_val]

	if(len(max_rel_index) > 1):
		card = []
		for i in max_rel_index:
			card.append(cardinality[i])

		min_val = min(card)
		min_card_index = D_card[min_val]
		if(len(min_card_index) > 1):
			for x in min_card_index:
				if(TG[x][0] not in T_temp):
					t = TG[x]
					return t
		else:
			t = TG[min_card_index[0]]
			return t

	else:
		t = TG[max_rel_index[0]]
		return t
		
def getUnionOfIntersection(input_list, av_pairs):
	result = set()
	for i in range(0, len(input_list)):
		if(i==0):
			result = get_intersection(input_list[i], av_pairs)
		else:
			result = result.union(get_intersection(input_list[i], av_pairs))
	return result


def get_intersection(input_list, av_pairs):
	input_list_values = []
	intersection_value = set()

	for av in input_list:
		input_list_values.append(av_pairs[av])
	
	if(len(input_list_values) == 1):
		intersection_value = input_list_values[0]
	else:
		for i in range(0, len(input_list_values)-1):
			if(i == 0):
				intersection_value = input_list_values[i].intersection(input_list_values[i+1])
			else:
				intersection_value = intersection_value.intersection(input_list_values[i+1])

	return intersection_value


def get_TG(av_pairs, G):
	TG = []
	for k, v in av_pairs.items():
		if(len(v.intersection(set(G))) != 0):
			TG.append(k)
	return TG

def mlem2(av_pairs, B):
	G = B
	Tou = []
	while(len(G) != 0):
		T = []
		TG = get_TG(av_pairs, G)
		while( len(T) == 0 or get_intersection(T, av_pairs).issubset(set(B)) == False):
			t = get_t(TG, av_pairs, G, T)
			T.append(t)
			G = av_pairs[t].intersection(set(G))
			TG = get_TG(av_pairs, G)
			for x in T:
				TG.remove(x)

		if(len(T) > 1):
			for i in T:
				T_copy = T[:]
				T_copy.remove(i)
				if(get_intersection(T_copy, av_pairs).issubset(set(B))):
					T.remove(i)

		Tou.append(T)
		G = set(B) - getUnionOfIntersection(Tou, av_pairs)
		

	for j in Tou:
		Tou_copy = Tou[:]
		Tou_copy.remove(j)
		if(getUnionOfIntersection(Tou_copy, av_pairs) == set(B)):
			Tou.remove(j)

	return Tou