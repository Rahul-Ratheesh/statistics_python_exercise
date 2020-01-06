import pylab, numpy

FILENAME = './data/actor_2013.csv'
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

ages = importData(FILENAME)
ageValues = [int(age) for age in ages['Age']]
desc = {}
desc['min'] = numpy.min(ageValues)
desc['Q1']  = numpy.quantile(ageValues, 0.25)
desc['median'] = numpy.median(ageValues)
desc['Q3']  = numpy.quantile(ageValues, 0.75)
desc['max'] = numpy.max(ageValues)
print(desc)