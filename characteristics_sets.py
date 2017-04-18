
def get_characteristic_sets(attributes, table, av_pairs):
	num_attr = len(attributes)-1
	inconsistent = set(['*', '?', '-'])
	k_sets = []

	for i in range(0, len(table)):
		case = table[i,:]

		temp = set()
		for j in range(0, num_attr):
			a = attributes[j]
			v = case[j]
			if(v not in inconsistent):
				if(len(temp) == 0):
					temp = av_pairs[(a,v)]	
				else:
					temp = temp.intersection(av_pairs[(a,v)])

		k_sets.append(temp)

	return k_sets




