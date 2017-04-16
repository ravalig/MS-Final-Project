import numpy as np

def createTable(filename):
	file = open(filename)

	file.readline()

	attributes = file.readline().split( )
	attributes.pop(0)
	attributes.pop()

	rows = []

	line = file.readline().split( )
	if(line[0] == '!'):
		pass

	while(line):
		if(line[0] != '!'):
			rows.append(line)
			line = file.readline().split( )

	num_columns = len(attributes)
	num_rows = len(rows)

	table = np.empty((0, num_columns))

	for i in rows:
		table = np.append(table, [i], axis=0)

	return table, attributes

