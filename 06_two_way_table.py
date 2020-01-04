import pylab, numpy

FILENAME = './data/nightlight.csv'
DELIMITER = ','

def importData(filename):
	data = {}
	with open(filename, 'r') as dataFile:
		headers = dataFile.readline().strip().split(DELIMITER)
		for header in headers:
			data[header] = []
		for line in dataFile:
			datarecord = line.strip().split(DELIMITER)
			for index, value in enumerate(datarecord):
				data[headers[index]].append(value)
	return data

def buildDataRecords(data):
	records = []
	for index, key in enumerate(data):
		records.append(data[key])
	table = {}
	for attribute_1, attribute_2 in list(zip(records[0], records[1])):
		if table.get(attribute_1) is None:
			table[attribute_1] = [attribute_2]
		else:
			table[attribute_1].append(attribute_2)
	return table

def buildPivotTable(attribute):
	props = {}
	for data in attribute:
		count = props.get(data)
		if count is None:
			props[data] = 1
		else:
			props[data] = count + 1
	return props

def buildTwoWayTable(table):
	twoWayTable = {}
	for index, key in enumerate(table):
		twoWayTable[key] = buildPivotTable(table[key])
	return twoWayTable

def buildPercentageTable(twoWayTable):
	percentTable = {}
	for row in twoWayTable:
		percentTable[row] = {}
		for col in twoWayTable[row]:
			percentTable[row][col] = round((twoWayTable[row][col] / sum(twoWayTable[row].values())) * 100, 2)
	return percentTable 

data = importData(FILENAME)
dataRecords = buildDataRecords(data)
twoWayTable = buildTwoWayTable(dataRecords)
percentTable = buildPercentageTable(twoWayTable)
print(percentTable)

responses = {}
for x in percentTable:
	for y in percentTable[x]:
		if responses.get(y) is None: 
			responses[y] = [percentTable[x][y]]
		else:
			responses[y].append(percentTable[x][y])
print(responses)
keys = list(responses.keys())
values = list(responses.values())
bar_width = 0.35
N = len(percentTable)
index = numpy.arange(N)

for i in range(len(values)):
	pylab.bar(index + bar_width*i, values[i], bar_width, label=keys[i])

pylab.title('Lighting Conditions and Near Sightedness')
pylab.xticks(index + bar_width, list(percentTable.keys()))
pylab.ylabel('Near Sightedness')
pylab.legend()
pylab.show()







