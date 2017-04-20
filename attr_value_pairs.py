import numpy as np
import collections

def add_to_avpair(a, v, i, av_pairs):
	if((a, v) not in av_pairs.keys()):
		av_pairs[(a, v)] = set()
		av_pairs[(a, v)].add(i)
	else:
		av_pairs[(a, v)].add(i)


def get_av_pairs(attributes, table):
	# print("In av_pairs method ") 
	# print(table)
	# print('\n')
	av_pairs = collections.OrderedDict()
	# print("Before getavpairs ") 
	# print(av_pairs)
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
				add_to_avpair(a, a_values[i], i, av_pairs)
			elif(a_values[i] == '?'):
				pass
			elif(a_values[i] == '*'):
				for j in range(0, len(a_unique_val)):
					add_to_avpair(a, a_unique_val[j], i, av_pairs)
			elif(a_values[i] == '-'):

				d = table[i,len(attributes)-1]
				val_set = set()

				for k in range(0, len(d_values)):
					if(d == d_values[k]):
						val = table[k,attr]				
						if(val not in inconsistent):
							val_set.add(val)			
				for x in val_set:
					add_to_avpair(a, x, i, av_pairs)	
	# print("After getavpairs ") 
	# print(av_pairs)
	# print('\n')
	return av_pairs