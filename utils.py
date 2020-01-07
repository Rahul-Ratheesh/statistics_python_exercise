import numpy

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

def groupBy(values, column):
	group = {}
	for value, col in zip(values, column):
		if group.get(col) is None:
			group[col] = [value]
		else:
			group[col].append(value)
	return group

def buildPivotTable(values):
	props = {}
	for data in values:
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

def fiveNumberSummary(values):
	return {
		'min': numpy.min(values),
		'Q1': numpy.quantile(values, 0.25),
		'median': numpy.median(values),
		'Q3': numpy.quantile(values, 0.75),
		'max': numpy.max(values)
	}
