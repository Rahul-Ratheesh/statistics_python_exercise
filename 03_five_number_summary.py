import pylab, numpy

FILENAME = './data/actor_2013.csv'
DELIMITER = ','

def importData(filename):
	with open(filename, 'r') as dataFile:
		headers = dataFile.readline().strip().split(DELIMITER)
		ages = []
		for line in dataFile:
			dataRecord = line.strip().split(DELIMITER)
			ages.append(int(dataRecord[0]))
	return ages

ages = importData(FILENAME)
desc = {}
desc['min'] = numpy.min(ages)
desc['Q1']  = numpy.quantile(ages, 0.25)
desc['median'] = numpy.median(ages)
desc['Q3']  = numpy.quantile(ages, 0.75)
desc['max'] = numpy.max(ages)
print(desc)