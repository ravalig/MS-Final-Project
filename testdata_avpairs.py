import numpy as np
import collections

def add_to_avpair1(a, v, i, av_pairs1):
	if(i not in av_pairs1.keys()):
		av_pairs1[i] = set()
		av_pairs1[i].add((a,v))
	else:
		av_pairs1[i].add((a,v))


def get_av_pairs1(attributes, table):
	# print("In av_pairs1 method ") 
	# print(table)
	# print('\n')
	av_pairs1 = collections.OrderedDict()
	# print("Before getavpairs ") 
	# print(av_pairs1)
	# print('\n')
	inconsistent = set(['*', '?', '-'])
	d_values = table[:,len(attributes)-1]

	num_attr = len(attributes) - 1
	for attr in range(0, num_attr):

		a = attributes[attr]
		a_values = table[:,attr]
		a_unique_val = list(set(a_values) - inconsistent)

		for i in range(0, len(a_values)):
			if(a_values[i] not in inconsistent):
				add_to_avpair1(a, a_values[i], i, av_pairs1)
			elif(a_values[i] == '?'):
				pass
			elif(a_values[i] == '*'):
				for j in range(0, len(a_unique_val)):
					add_to_avpair1(a, a_unique_val[j], i, av_pairs1)
			elif(a_values[i] == '-'):

				d = table[i,len(attributes)-1]
				val_set = set()

				for k in range(0, len(d_values)):
					if(d == d_values[k]):
						val = table[k,attr]				
						if(val not in inconsistent):
							val_set.add(val)			
				for x in val_set:
					add_to_avpair1(a, x, i, av_pairs1)	
	return av_pairs1