import pylab, numpy

FILENAME = './data/animals.csv'
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

data = importData(FILENAME)
gestations = [int(gestation) for gestation in data['gestation']]
longevitys = [int(longevity) for longevity in data['longevity']]
print(numpy.corrcoef(gestations, longevitys))

figure = pylab.figure()    
plot = figure.add_subplot(1, 1, 1)
pylab.scatter(gestations, longevitys, color = 'steelblue')
pylab.title('Gestation vs Longevity in Animals')
pylab.xlabel('Gestation')
pylab.ylabel('Longevity')
plot.set_axisbelow(True)
plot.yaxis.grid(color = 'gray', linestyle = 'solid', alpha = 0.5)
pylab.show()