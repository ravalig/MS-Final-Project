from collections import defaultdict
from attr_value_pairs import get_av_pairs
from characteristics_sets import get_characteristic_sets

class LEM2(object):
	"""docstring for LEM2"""
	table = []
	attributes = []
	av_pairs = {}
	k_sets = []

	def __init__(self, table, attributes):
		self.table = table
		self.attributes = attributes

	def mlem2(self, B):
		self.av_pairs = get_av_pairs(self.attributes, self.table)
		self.k_sets = get_characteristic_sets(self.attributes, self.table, self.av_pairs)

		G = B
		Tou = []
		while(len(G) != 0):
			T = []
			TG = self.get_TG(G)
			while( len(T) == 0 or self.get_intersection(T).issubset(set(B)) == False):
				t = self.get_t(TG, G, T)
				T.append(t)
				G = self.av_pairs[t].intersection(set(G))
				TG = self.get_TG(G)
				for x in T:
					TG.remove(x)

			if(len(T) > 1):
				for i in T:
					T_copy = T[:]
					T_copy.remove(i)
					if(self.get_intersection(T_copy).issubset(set(B))):
						T.remove(i)

			Tou.append(T)
			G = set(B) - self.getUnionOfIntersection(Tou)
		

		for j in Tou:
			Tou_copy = Tou[:]
			Tou_copy.remove(j)
			if(self.getUnionOfIntersection(Tou_copy) == set(B)):
				Tou.remove(j)

		return Tou


	def get_t(self, TG, G, T):
		T_temp = []
		for l in T:
			T_temp.append(l[0])

		relevance = []
		cardinality = []
		for av in TG:
			relevance.append(len(self.av_pairs[av].intersection(set(G))))
			cardinality.append(len(self.av_pairs[av]))
	
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


	def getUnionOfIntersection(self, input_list):
		result = set()
		for i in range(0, len(input_list)):
			if(i==0):
				result = self.get_intersection(input_list[i])
			else:
				result = result.union(self.get_intersection(input_list[i]))
		return result

	def get_intersection(self, input_list):
		input_list_values = []
		intersection_value = set()

		for av in input_list:
			input_list_values.append(self.av_pairs[av])
	
		if(len(input_list_values) == 1):
			intersection_value = input_list_values[0]
		else:
			for i in range(0, len(input_list_values)-1):
				if(i == 0):
					intersection_value = input_list_values[i].intersection(input_list_values[i+1])
				else:
					intersection_value = intersection_value.intersection(input_list_values[i+1])

		return intersection_value


	def get_TG(self, G):
		TG = []
		for k, v in self.av_pairs.items():
			if(len(v.intersection(set(G))) != 0):
				TG.append(k)
		return TG








		