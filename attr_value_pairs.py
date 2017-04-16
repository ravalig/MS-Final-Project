import numpy as np

av_pairs = {}

def add_to_avpair(a, v, i):

	if((a, v) not in av_pairs.keys()):
		av_pairs[(a, v)] = set()
		av_pairs[(a, v)].add(i)
	else:
		av_pairs[(a, v)].add(i)


def calculate_av_pairs(attributes, table):
	inconsistent = set(['*', '?', '-'])
	d_values = table[:,len(attributes)-1]

	num_attr = len(attributes) - 1
	for attr in range(0, num_attr):

		a = attributes[attr]
		a_values = table[:,attr]
		a_unique_val = list(set(a_values) - inconsistent)


		for i in range(0, len(a_values)):
			if(a_values[i] not in inconsistent):
				add_to_avpair(a, a_values[i], i)
			elif(a_values[i] == '?'):
				pass
			elif(a_values[i] == '*'):
				for j in range(0, len(a_unique_val)):
					add_to_avpair(a, a_unique_val[j], i)
			elif(a_values[i] == '-'):

				d = table[i,len(attributes)-1]
				val_set = set()

				for k in range(0, len(d_values)):
					if(d == d_values[k]):
						print(d_values[k])
						val = table[k,attr]				# Replace wind attribute 0 with corresponding value
						if(val not in inconsistent):
							val_set.add(val)
			
				for x in val_set:
					add_to_avpair(a, x, i)		

	print(av_pairs)