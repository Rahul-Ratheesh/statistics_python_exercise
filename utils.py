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

def buildPivotTable(values):
	props = {}
	for data in values:
		count = props.get(data)
		if count is None:
			props[data] = 1
		else:
			props[data] = count + 1
	return props

def fiveNumberSummary(values):
	return {
		'min': numpy.min(values),
		'Q1': numpy.quantile(values, 0.25),
		'median': numpy.median(values),
		'Q3': numpy.quantile(values, 0.75),
		'max': numpy.max(values)
	}
